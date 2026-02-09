# Seed Survey — Capture Template

Use during Session 001 to log responses and know where each goes.

---

## Pre-Session Checklist

- [ ] SELF.md identity fields filled (name, birthdate, languages, location) — if known
- [ ] Parent has read docs/PARENT-BRIEF.md
- [ ] Consent logged in SESSION-LOG.md
- [ ] Capture method ready (parent typing / voice + transcribe)

---

## Question → Destination Map

| # | Question | SELF.md destination | Notes |
|---|----------|---------------------|-------|
| 1 | Favorite movies/shows? | `II.PREFERENCES.movies` | List as provided |
| 2 | Favorite books/stories? | `II.PREFERENCES.books` | List as provided |
| 3 | Favorite places? | `II.PREFERENCES.places` | List as provided |
| 4 | Favorite games? | `II.PREFERENCES.games` | List as provided |

---

## Capture (fill during session)

### Q1: Favorite movies or shows?
```
[Responses]
```

### Q2: Favorite books or stories?
```
[Responses]
```

### Q3: Favorite places?
```
[Responses]
```

### Q4: Favorite games?
```
[Responses]
```

---

## Post-Session Updates

1. **SELF.md** — Paste responses into `II. PREFERENCES > Favorites` YAML:
   ```yaml
   movies: [list from Q1]
   books: [list from Q2]
   places: [list from Q3]
   games: [list from Q4]
   ```
2. **SELF.md** — Set `survey_completed: true` in XII. METADATA
3. **SESSION-LOG.md** — Add SESSION 001 block with date, participants, responses, updates
4. **SURVEY-CAPTURE.md** — Optional: keep for reference or delete after data migrated
