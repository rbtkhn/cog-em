# LIBRARY Schema

**Purpose:** Governs the LIBRARY component — the prioritized list of books/sources Grace-Mar must query first when answering questions. Only if the answer is not found in LIBRARY does the system fall back to full LLM lookup or web search.

**See also:** [ARCHITECTURE.md](ARCHITECTURE.md), [ID-TAXONOMY.md](ID-TAXONOMY.md), EVIDENCE § I. READING LIST

---

## Relationship to Reading List

| Component | Purpose |
|-----------|---------|
| **EVIDENCE Reading List (READ-*)** | Books Grace-Mar has *consumed* — evidence of what she's read |
| **LIBRARY** | Approved sources for *lookup* — what she can query when answering questions |

A book can appear in both. LIBRARY can also include reference sources she hasn't read but are parent-approved for lookup (e.g., encyclopedia, science reference).

---

## Entry Format

Each LIBRARY entry uses the **LIB-** prefix.

```yaml
entries:
  - id: LIB-0001
    title: "Example Book Title"
    author: "Author Name"
    isbn: ""                      # optional: 10- or 13-digit ISBN (for lookup, disambiguation)
    type: book                    # book | article | reference | other
    status: active                # active | deprecated
    scope: []                     # optional: topics this source covers (for query routing)
    read_id: null                 # optional: READ-XXXX if also in Reading List
    source: manual                # manual | path | url (for future RAG/indexing)
    added_at: 2026-02-XX
    notes: ""                     # optional
```

---

## Fields

| Field | Required | Description |
|-------|----------|-------------|
| **id** | Yes | LIB-NNNN (4-digit zero-padded) |
| **title** | Yes | Full title |
| **author** | No | Author or editor (omit for reference works) |
| **isbn** | No | 10- or 13-digit ISBN (with or without hyphens). Use for catalog lookups, disambiguation, future RAG. Older or non-trade books may omit. |
| **type** | Yes | `book`, `article`, `reference`, `other` |
| **status** | Yes | `active` (queryable) or `deprecated` (excluded from lookup) |
| **scope** | No | List of topics (e.g. `[space, science, animals]`) for query routing |
| **read_id** | No | READ-XXXX if this book is in EVIDENCE Reading List |
| **source** | Yes | `manual` (no indexed content yet), `path`, or `url` for future RAG |
| **added_at** | Yes | ISO date when added |
| **notes** | No | Free-form notes |

---

## ISBN Notes

- Store digits with or without hyphens. Normalize to ISBN-13 when both formats exist.
- Use for: catalog lookups (Open Library, WorldCat), disambiguation between editions, future RAG indexing.

---

## Lookup Order

When Grace-Mar receives a question:

1. **Query LIBRARY** (active entries only, ordered by priority or scope match)
2. **If found** → Answer from LIBRARY, rephrase in Grace-Mar's voice
3. **If not found** → "I haven't learned that yet! do you want me to look it up?" → fall back to full LOOKUP

---

## Governance

- LIBRARY entries are added only through the gated pipeline or explicit user action
- Deprecating a source: set `status: deprecated`; do not delete (history preserved)
- New entries get `added_at`; optional `evidence_tier` if linked to READ-*

---

## ID Allocation

LIB-* IDs are allocated sequentially. Next ID = max(LIB-*) + 1.

---

*Last updated: February 2026*
