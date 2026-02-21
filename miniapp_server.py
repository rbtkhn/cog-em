#!/usr/bin/env python3
"""
Grace-Mar Q&A Mini App server.

Serves the interactive Q&A Mini App and provides the /api/ask endpoint.
Deploy to Railway, Render, or run locally with ngrok for Telegram testing.

Usage:
    pip install flask python-dotenv openai
    OPENAI_API_KEY=... python miniapp_server.py

Set PORT (default 5000) for hosting. Enable CORS if Mini App is on a different origin.
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from flask import Flask, jsonify, request, send_from_directory

REPO_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO_ROOT))

load_dotenv(REPO_ROOT / ".env")
load_dotenv(REPO_ROOT / "bot" / ".env")

from openai import OpenAI

from bot.prompt import SYSTEM_PROMPT
from bot.core import (
    run_lookup,
    LOOKUP_TRIGGER,
    AFFIRMATIVE_WORDS,
    AFFIRMATIVE_PHRASES,
)

app = Flask(__name__, static_folder="miniapp", static_url_path="")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")


def _is_affirmative(text: str) -> bool:
    normalized = text.strip().lower().rstrip("!.,")
    return normalized in AFFIRMATIVE_WORDS or any(p in normalized for p in AFFIRMATIVE_PHRASES)


def _last_user_message_before(history: list, before_index: int) -> str | None:
    """Return the last user message before the given index."""
    for i in range(before_index - 1, -1, -1):
        if history[i].get("role") == "user":
            return (history[i].get("content") or "").strip()
    return None


def _should_run_lookup(message: str, history: list) -> str | None:
    """If this is an affirmative follow-up to a lookup offer, return the question to look up."""
    if not history or len(history) < 2:
        return None
    last = history[-1]
    if last.get("role") != "assistant":
        return None
    last_content = (last.get("content") or "").strip()
    if LOOKUP_TRIGGER not in last_content.lower():
        return None
    if not _is_affirmative(message):
        return None
    question = _last_user_message_before(history, len(history))
    return question if question else None


@app.route("/")
def index():
    return send_from_directory("miniapp", "index.html")


@app.after_request
def _cors(resp):
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return resp


@app.route("/api/ask", methods=["POST", "OPTIONS"])
def ask():
    if request.method == "OPTIONS":
        return "", 204
    if not OPENAI_API_KEY:
        return jsonify({"error": "OPENAI_API_KEY not configured"}), 500
    data = request.get_json() or {}
    message = (data.get("message") or "").strip()
    if not message:
        return jsonify({"error": "message required"}), 400
    history = data.get("history") or []

    try:
        # Affirmative follow-up to "do you want me to look it up?" → run lookup
        question = _should_run_lookup(message, history)
        if question:
            reply = run_lookup(question, channel_key="miniapp")
            return jsonify({"response": reply})

        # Normal flow: SYSTEM_PROMPT + history + new message
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        for h in history:
            role = h.get("role")
            content = (h.get("content") or "").strip()
            if role in ("user", "assistant") and content:
                messages.append({"role": role, "content": content})
        messages.append({"role": "user", "content": message})

        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            max_tokens=200,
            temperature=0.9,
        )
        reply = response.choices[0].message.content.strip()
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
