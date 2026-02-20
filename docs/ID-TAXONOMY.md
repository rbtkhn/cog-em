# ID Taxonomy

**Purpose:** Canonical reference for all identifier prefixes used in Grace-Mar. Ensures consistent naming and supports provenance, schema work, and tooling.

**See also:** [ARCHITECTURE.md](ARCHITECTURE.md), [PIPELINE-MAP.md](PIPELINE-MAP.md)

---

## Prefix Summary

| Prefix | Scope | Location | Description |
|--------|-------|----------|-------------|
| **ACT-** | Activity | EVIDENCE.md § V. ACTIVITY LOG | Raw activity records — bot exchanges, physical artifacts, lookups |
| **LEARN-** | Knowledge | SELF.md IX-A | Facts that entered awareness (post-seed) |
| **CUR-** | Curiosity | SELF.md IX-B | Topics that caught attention (post-seed) |
| **PER-** | Personality | SELF.md IX-C | Observed behavioral patterns (post-seed) |
| **CANDIDATE-** | Pipeline | PENDING-REVIEW.md | Staged signals awaiting approve/reject |
| **WRITE-** | Evidence | EVIDENCE.md § II. WRITING LOG | Writing samples, journals, stories |
| **READ-** | Evidence | EVIDENCE.md § I. READING LIST | Books, articles consumed |
| **CREATE-** | Evidence | EVIDENCE.md § III. CREATION LOG | Artwork, collages, creative output |
| **MEDIA-** | Evidence | EVIDENCE.md § IV. MEDIA LOG | Movies, shows, games (survey + mentions) |
| **LIB-** | Library | users/[id]/LIBRARY.md | Approved lookup sources (query first before full LLM) |

---

## Relationships

```
CANDIDATE-* (pending)
    │
    ├──[approved]──► ACT-* (new) + LEARN-* | CUR-* | PER-* (new)
    │
    └──[rejected]──► (no new IDs)

ACT-*
    │
    └──[referenced by]──► LEARN-*, CUR-*, PER-* (via evidence_id)

WRITE-*, CREATE-*, READ-*
    │
    └──[referenced by]──► SELF (seed/post-seed), SKILLS, activity_id in samples
```

---

## Format

- **ACT-NNNN** — 4-digit zero-padded (ACT-0001, ACT-0014)
- **LEARN-NNNN**, **CUR-NNNN**, **PER-NNNN** — 4-digit zero-padded
- **CANDIDATE-NNNN** — 4-digit zero-padded
- **WRITE-NNNN**, **READ-NNNN**, **CREATE-NNNN** — 4-digit zero-padded
- **MEDIA-NNNN** — 4-digit zero-padded

---

## Evidence References

Every post-seed SELF entry (IX-A, IX-B, IX-C) must have `evidence_id: ACT-XXXX` pointing to an existing Activity Log entry. This enforces:

- No claim without evidence
- LLM knowledge cannot leak (claims require user-approved source)
- Provenance is traceable

---

## Allocation

| ID type | Allocated by |
|---------|--------------|
| ACT-* | Integration step (when processing approved candidates) or manual evidence entry |
| LEARN-, CUR-, PER-* | Integration step (derived from CANDIDATE) |
| CANDIDATE-* | `bot/bot.py` `_next_candidate_id()` when analyst stages |
| LIB-* | Manual entry in LIBRARY |
| WRITE-, READ-, CREATE-* | Manual entry in EVIDENCE |
| MEDIA-* | Survey seed or manual entry |

---

*Last updated: February 2026*
