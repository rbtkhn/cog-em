# SELF–TEMPLATE v1.0

Cognitive Emulator · Self Module Governance Template

Status: DRAFT
Version: 1.0
Last Update: February 2026

Adapted from: CIV–MIND–TEMPLATE v3.0 (CMC)

---

## I. PURPOSE

This template governs the SELF module of the cognitive twin.

The SELF module:
- Captures WHO the student IS
- Mirrors personality, linguistic style, values, narrative
- Enables authentic emulation (not idealization)
- Evolves as the student grows
- Allows recognition by those who know the student

The SELF module is NOT:
- A curated persona
- An idealized version
- A generic child profile
- A static personality test result

SELF strives for AUTHENTIC MIRRORING.

---

## II. CORE PRINCIPLE: AUTHENTIC MIRRORING

The twin should mirror the student as they actually are.

### Include

- Actual vocabulary (including "um", "like", filler words)
- Real preferences (even embarrassing ones)
- Actual reasoning patterns (including biases)
- Their version of events (not objective third-party)
- Quirks and imperfections
- Verbal habits and catchphrases

### Exclude

- Polished, idealized speech
- Curated, socially-desirable answers
- Corrected, "better" reasoning
- Normalized, generic personality

### Validation Test (Recognition)

The SELF module is working when:
- The student recognizes themselves in the twin
- Others who know the student recognize them through the twin

If a parent, teacher, or friend says "that sounds exactly like them" — success.
If they say "that doesn't sound like them" — failure.

---

## III. SELF COMPONENTS

### 1. Identity

Basic information about the student.

```typescript
identity: {
  name: string;
  birthdate: Date;
  age: number;                    // Calculated
  languages: string[];
  location: string;
  created_at: Date;
}
```

### 2. Personality

Observable behavioral tendencies.

```typescript
personality: {
  traits: {
    trait: string;               // e.g., "curious", "cautious"
    confidence: number;          // 0-1
    evidence: string[];          // Sessions that revealed this
  }[];
  
  emotional_patterns: {
    trigger: string;             // What triggers the emotion
    response: string;            // How they typically respond
    examples: string[];
  }[];
  
  updated_at: Date;
}
```

### 3. Linguistic Style

How they communicate. **Primary data source: WRITE activities.**

```typescript
linguistic_style: {
  vocabulary_level: number;      // Age-adjusted, derived from WRITE.vocabulary
  
  sentence_patterns: {
    pattern: string;             // e.g., "starts with 'so'"
    frequency: number;
    examples: string[];          // From WRITE activities
  }[];
  
  verbal_habits: string[];       // "um", "like", catchphrases
  
  tone: string;                  // e.g., "enthusiastic", "quiet"
  
  samples: {
    content: string;             // Actual quote from WRITE activity
    date: Date;
    activity_id: string;         // Reference to source activity
    context: string;
  }[];
  
  // Derivation metadata
  derived_from: {
    activity_count: number;      // How many WRITE activities analyzed
    last_updated: Date;
  };
  
  updated_at: Date;
}
```

**Derivation pipeline:**
```
WRITE Activity (journal, story, message)
    │
    └── Text analyzed for:
        ├── Vocabulary (unique words, sophistication)
        ├── Sentence patterns (structure, length)
        ├── Verbal habits (repeated phrases)
        ├── Tone (emotional register)
        └── Notable samples (added to archive)
            │
            └── SELF.linguistic_style updated
```

The more WRITE activities, the richer the linguistic fingerprint.

### 4. Life Narrative

Their story, memories, relationships.

```typescript
narrative: {
  family: {
    members: {
      name: string;
      relationship: string;      // "mom", "grandpa", "sister"
      notes: string;             // How student describes them
    }[];
    dynamics: string;            // Student's view of family
  };
  
  places: {
    birthplace: string;
    places_lived: {
      place: string;
      period: DateRange;
      significance: string;      // What it means to them
    }[];
    favorite_places: string[];
  };
  
  significant_events: {
    event: string;
    date: Date;
    impact: string;              // How it affected them
    their_version: string;       // How THEY tell the story
  }[];
  
  relationships: {
    name: string;
    nature: string;              // "best friend", "teacher"
    significance: string;
  }[];
  
  memories: {
    content: string;
    date_added: Date;
    emotional_tone: string;
  }[];
}
```

### 5. Preferences

Likes, dislikes, tastes. **Primary data source: READ activities + explicit input.**

```typescript
preferences: {
  favorites: {
    movies: string[];
    books: string[];             // Derived from READ content log
    music: string[];
    places: string[];
    activities: string[];
    foods: string[];
    people: string[];            // Characters, heroes, family
    [custom]: string[];          // Extensible
  };
  
  dislikes: string[];
  
  happiness_triggers: string[];
  frustration_triggers: string[];
  
  learning_preferences: {
    modality: string;            // visual, auditory, kinesthetic
    environment: string;         // quiet, music, etc.
    time_of_day: string;
  };
  
  // Derivation metadata
  derived_from: {
    read_activity_count: number;
    explicit_input_count: number;
    last_updated: Date;
  };
  
  updated_at: Date;
}
```

**Derivation from READ:**
```
READ Activity Log
    │
    ├── Books read → preferences.favorites.books
    ├── Re-reads detected → strong preference signal
    ├── Genres chosen → interest patterns
    ├── Themes returned to → values inference
    └── Content avoided → dislikes inference
```

Preferences combine explicit input (survey) + inferred from READ behavior.

### 6. Values

What matters to them.

```typescript
values: {
  core: string[];                // e.g., "fairness", "family"
  
  inferred_from: {
    value: string;
    evidence: string[];          // What revealed this value
  }[];
  
  conflicts: {
    value_a: string;
    value_b: string;
    context: string;             // When these conflict
  }[];
  
  updated_at: Date;
}
```

### 7. Reasoning Patterns

How they think.

```typescript
reasoning_patterns: {
  style: string;                 // visual, sequential, intuitive
  
  approach_to_new: string;       // How they handle new things
  approach_to_hard: string;      // How they handle difficulty
  approach_to_conflict: string;  // How they handle disagreement
  
  characteristic_moves: {
    situation: string;
    typical_response: string;
    examples: string[];
  }[];
  
  updated_at: Date;
}
```

### 8. Interests

What captures their attention. **Derived from all three pillars.**

```typescript
interests: {
  current: {
    topic: string;
    intensity: number;           // 1-5
    since: Date;
    sources: string[];           // Which pillars revealed this
  }[];
  
  historical: {
    topic: string;
    period: DateRange;
    peak_intensity: number;
  }[];
  
  emerging: string[];            // Topics showing new interest
  declining: string[];           // Topics losing interest
  
  // Derivation metadata
  derived_from: {
    write_topics: number;        // Topics from WRITE content
    read_content: number;        // Topics from READ choices
    imagine_themes: number;      // Topics from IMAGINE activities
    last_updated: Date;
  };
}
```

**Derivation from all pillars:**
```
WRITE: topics written about → interests
READ: content chosen → interests  
IMAGINE: themes explored → interests

Example:
├── WRITE: 12 journal entries mention "dinosaurs"
├── READ: 3 dinosaur books, 1 dinosaur video
├── IMAGINE: 5 creative plays involving dinosaurs
│
└── SELF.interests: { topic: "dinosaurs", intensity: 5, sources: ["WRITE", "READ", "IMAGINE"] }
```

---

## IV. SELF SEEDING (INITIAL SURVEY)

For a 6-year-old starting the system.

### Survey Questions

1. **Favorites**
   - What are your favorite movies or shows? (up to 10)
   - What are your favorite books or stories? (up to 10)
   - What are your favorite places to go? (up to 10)
   - What are your favorite things to do? (up to 10)
   - Who are your favorite people? (family, friends, characters)

2. **Emotions**
   - What makes you really happy?
   - What makes you frustrated or upset?
   - What are you scared of?
   - What makes you excited?

3. **Learning**
   - How do you like to learn new things?
   - Do you like to figure things out yourself or have someone show you?
   - Do you like to work alone or with others?

4. **Identity**
   - Tell me about your family
   - Where do you live? Where have you lived?
   - What do you want to be when you grow up?

5. **Open**
   - What else should your learning friend know about you?

### Survey Administration

- Can be voice-recorded (transcribed)
- Parent may assist for young children
- Answers are SEEDING, not permanent
- All answers are preferences, not tests

---

## V. SELF EVOLUTION

Unlike CMC's frozen MIND profiles, SELF evolves.

### What Evolves

- Preferences change (6-year-old → 16-year-old)
- Linguistic style matures
- Reasoning patterns develop
- Interests shift
- Values deepen

### How It Evolves

1. **Continuous Inference**
   - System observes how student teaches
   - Patterns detected and recorded
   - Confidence scores updated

2. **Periodic Anchoring**
   - Annual or milestone surveys
   - Parent/teacher attestation
   - Student self-reflection

3. **Explicit Updates**
   - Student says "I don't like that anymore"
   - Parent provides correction
   - Major life event

### Preserving History

Changes do NOT overwrite. History is preserved.

```
PREFERENCE HISTORY: Favorite Movie

2026-03 (age 6): Frozen
2027-09 (age 7): Moana
2029-01 (age 9): Harry Potter
2031-06 (age 11): Star Wars
```

The twin knows current preference AND can recall past preferences.

---

## VI. FORBIDDEN BEHAVIORS

What the twin should NOT say or do (based on SELF).

Adapted from CMC's Forbidden Linguistic Behaviors.

### Capture Negative Markers

```typescript
forbidden: {
  phrases_never_used: string[];    // Words they don't use
  tones_never_adopted: string[];   // Tones foreign to them
  reasoning_never_used: string[];  // Ways they don't think
}
```

### Purpose

- Prevents generic responses
- Ensures twin sounds like THIS student
- Detection mechanism for authenticity

### Example

```
FORBIDDEN for [Student]:
- Never uses: "furthermore", "consequently" (too formal)
- Never adopts: sarcastic tone (earnest personality)
- Never reasons: abstract-first (always starts concrete)
```

---

## VII. SNAPSHOTS

Preserve SELF at points in time.

### Snapshot Triggers

- Age milestones (6, 8, 10, 12, 14, 16, 18)
- Major life transitions
- Annual archival
- On-demand

### Snapshot Format

```
SELF–SNAPSHOT–[NAME]–AGE–[X]

Created: [YYYY-MM-DD]
Status: ARCHIVED

PERSONALITY SUMMARY:
[Key traits at this age]

LINGUISTIC MARKERS:
[How they spoke at this age]

FAVORITES AT THIS AGE:
[Top preferences]

VALUES:
[What mattered to them]

INTERESTS:
[What captured their attention]

NARRATIVE:
[Their story up to this point]
```

### Preservation Rule

Snapshots are IMMUTABLE.
Parent can revisit "who they were at 6."
Student can see their own growth.

---

## VIII. QUERYING SELF

How the twin uses SELF to respond.

### For Emulation

When asked "What would [student] say about X?":
1. Load relevant SELF components
2. Apply linguistic style
3. Filter through values
4. Reason in their pattern
5. Deliver in their voice

### For Recognition

When evaluator queries:
- "What kind of person is [student]?" → Personality summary
- "How does [student] communicate?" → Linguistic markers
- "What does [student] care about?" → Values and interests
- "Tell me about [student]'s background" → Life narrative

### For Prediction

When asked "What would [student] enjoy?":
- Use preferences and interests
- Apply reasoning patterns
- Consider values alignment
- Deliver suggestion in their voice

---

## IX. PRIVACY TIERS

SELF is highly sensitive.

### Access Levels

| Accessor | Access Level |
|----------|--------------|
| Student | Full |
| Parent (child <12) | Full |
| Parent (child 12-16) | Summary + explicit grants |
| Parent (child 16+) | Summary only |
| Parent (child 18+) | None unless granted |
| Employer | None unless granted (rare) |
| University | None unless granted (rare) |
| Mentor | Granted portions only |

### What Can Be Shared

- SKILLS can be shared without SELF
- SELF sharing is always opt-in
- Granular control (share interests, not values)
- Time-limited access

---

## X. COMPLIANCE CHECKLIST

Before marking SELF as initialized:

- [ ] Identity complete
- [ ] Initial survey completed
- [ ] At least 5 preferences captured
- [ ] Language samples collected (5+)
- [ ] Basic personality traits inferred
- [ ] Family/narrative basics captured

Before creating SELF SNAPSHOT:

- [ ] All components reviewed
- [ ] Historical changes preserved
- [ ] Linguistic samples current
- [ ] Personality confidence scores assigned
- [ ] Interests updated
- [ ] Timestamp recorded
- [ ] Marked as ARCHIVED (immutable)

---

## XI. INTEGRATION WITH SKILLS

### SELF → SKILLS

- Learning preferences (SELF) shape how knowledge is organized
- Interests (SELF) predict which domains develop
- Reasoning patterns (SELF) affect concept connections

### SKILLS → SELF

- What student teaches reveals interests
- How they explain reveals linguistic style
- Struggles reveal emotional patterns

### Full Emulation Requires Both

> "Explain [topic] the way [student] would"

= SKILLS (what they know) + SELF (how they express it)

---

END OF FILE — SELF–TEMPLATE v1.0
