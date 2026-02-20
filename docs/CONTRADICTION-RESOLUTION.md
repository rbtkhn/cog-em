# Contradiction Resolution

**Purpose:** Define how to handle conflicts between new evidence and existing SELF/SKILLS claims. Preserves history instead of overwriting; requires explicit user resolution.

**Status:** Specification for approved improvement #2 (Contradiction surfacing). Not yet implemented.

**See also:** [ANTI-CHEATING.md](ANTI-CHEATING.md), [AGENTS.md](../AGENTS.md) (immutability rules)

---

## Principle

When new evidence contradicts an existing claim, do **not** overwrite. Instead:

1. Surface the conflict
2. Preserve both the old claim and the new evidence
3. Record the user's resolution
4. Optionally supersede the old claim with a resolution pointer

---

## Resolution Record Format

When a conflict is resolved, record:

```yaml
superseded_entry:
  id: LEARN-0024                    # or CUR-*, PER-*
  original_claim: "fearful of swimming"
  superseded_at: 2026-02-25
  superseded_by: ACT-0015           # evidence that contradicted
  resolution: growth                # user-chosen resolution type
  resolution_note: "Overcame fear; joined swim team. Growth, not contradiction."
```

### Resolution Types

| Type | Meaning |
|------|---------|
| **growth** | The new evidence shows development; old claim was true then, new is true now |
| **correction** | The old claim was wrong; new evidence corrects it |
| **context** | Both can be true in different contexts; keep both with clarification |
| **reject_new** | User rejects the new evidence; keep old claim |
| **exception** | Edge case; document why both coexist |

---

## Conflict Detection (Future)

A contradiction detector would:

1. Compare new candidate content to existing SELF IX-A/B/C entries
2. Flag semantic conflicts (e.g., "fearful of swimming" vs "joined swim team")
3. Stage conflict for user resolution instead of auto-integrating
4. On resolution, add `superseded_by` / `superseded_entry` to old claim, add new claim with `supersedes: LEARN-XXXX`

---

## Temporal Validity (Future)

When temporal validity layer (#3) is implemented, resolved claims get:

- `valid_from: 2026-02-19`
- `valid_until: 2026-02-25` (or `superseded_by` reference)
- `superseded_by: LEARN-0025` (the new claim that replaces this one)

The fork state at time T is computed by filtering entries where `valid_from <= T` and `valid_until` is null or `> T`.

---

## Example

**Before (conflict detected):**

- SELF IX-C: "Fearful of swimming (deep water) — WRITE-0003"
- New candidate: "Joined swim team — observed at pool"

**After resolution (type: growth):**

- Old entry gets `superseded_by: ACT-0015`, `resolution: growth`
- New entry: PER-0002 "Overcame swimming fear; joined team — ACT-0015"
- History preserved: both the fear and the growth are in the record

---

*Last updated: February 2026*
