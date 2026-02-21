# Telegram Mini App Setup

Grace-Mar has two web surfaces:

- **Dashboard** — Full profile view (Knowledge, Skills, Curiosity, Personality, Library, Disclosure). **Browser only.** Served on GitHub Pages.
- **Q&A Mini App** — Interactive Q&A with Grace-Mar. Runs as a **Telegram Mini App** and can also be opened in a browser.

## Architecture

| Surface | Host | URL | Purpose |
|---------|------|-----|---------|
| Dashboard | GitHub Pages | `https://<org>.github.io/grace-mar/dashboard/` | Read-only fork view, browser-only |
| Q&A Mini App | Railway / Render / etc. | `https://grace-mar-qa.railway.app` | Ask Grace-Mar questions, see her knowledge and voice |

Set `DASHBOARD_MINIAPP_URL` in `bot/.env` to the **Q&A Mini App** URL (not the dashboard). The menu button and `/dashboard` open the Q&A app inside Telegram.

## 1. Dashboard (browser-only)

Generate and deploy the static dashboard:

```bash
python3 scripts/generate_dashboard.py
```

Deploy `dashboard/` to GitHub Pages via `.github/workflows/pages.yml`. The dashboard lives at `https://<org>.github.io/grace-mar/dashboard/`. Users open it directly in a browser.

## 2. Q&A Mini App (Mini App + API)

The Q&A app consists of:

- Static UI: `miniapp/index.html`
- API: `POST /api/ask` with `{ "message": "..." }` → `{ "response": "..." }`
- Server: `miniapp_server.py` serves both

### Run locally

```bash
pip install -r requirements.txt
OPENAI_API_KEY=sk-... python miniapp_server.py
```

Open http://localhost:5000. For Telegram testing, expose with ngrok:

```bash
ngrok http 5000
```

### Deploy (Railway / Render)

**Railway**

1. Connect the repo.
2. Root directory = repo root. Railway uses `Procfile` and `requirements.txt`.
3. Set env: `OPENAI_API_KEY`, `PORT` (optional, Railway sets it).
4. Deploy. Use the generated URL (e.g. `https://grace-mar-qa.railway.app`).

**Render**

1. New Web Service, connect repo.
2. Build: `pip install -r requirements.txt`
3. Start: `python miniapp_server.py`
4. Set `OPENAI_API_KEY`. Use the service URL.

## 3. Configure the bot (.env)

```env
DASHBOARD_MINIAPP_URL=https://grace-mar-qa.railway.app
```

This URL must serve the Q&A Mini App (HTML at `/`, API at `/api/ask`). When set, the bot exposes `/dashboard` and the menu button, both opening this Q&A app.

## 4. @BotFather (optional)

In @BotFather → Bot Settings → Menu Button:

- Set URL to your Q&A Mini App URL (same as `DASHBOARD_MINIAPP_URL`).

## 5. Deep linking

Use `startapp` to open the Q&A app:

- `t.me/your_bot?startapp=` — opens the Q&A Mini App.

## Security

- The Q&A API is stateless and uses the same `SYSTEM_PROMPT` as the bot. No profile writes from the Mini App.
- For production, consider rate limiting and `initData` validation (HMAC-SHA-256 with bot token) if you need user verification.
