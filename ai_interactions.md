# AI Interactions Log

This file documents how AI supported the optional stretch features in the Music Recommender Simulation project. I used AI for brainstorming, generating sample values, suggesting modular designs, and checking logic. I manually reviewed all generated changes, ran the program, inspected the output, and verified the project with `pytest`.

---

## Agentic Workflow

### What task did I give the AI?

I asked the AI to help extend the recommender across several files. The work included adding new song attributes to the CSV, updating the loader and scoring logic, adding multiple scoring modes, implementing an artist diversity penalty, and improving the terminal output.

### Prompts Used

Examples of prompts I used:

> Generate realistic values for five new song attributes: popularity, release decade, instrumentalness, liveness, and speechiness. Keep the existing song data unchanged and use valid ranges for each new feature.

> Help me design multiple scoring modes for my music recommender while keeping the code modular. I want Genre-First, Mood-First, and Energy-Focused modes without duplicating the whole scoring algorithm.

> Help me add a diversity penalty. If an artist is already represented in the selected recommendations, reduce the score of additional songs by that artist. Recalculate the remaining candidates after every selection.

> Suggest a clean way to display recommendation results in a terminal table that includes song title, score, and reasons.

### What did the AI generate or change?

The AI helped me plan and implement changes in:

* `data/songs.csv`
* `src/recommender.py`
* `src/main.py`
* `requirements.txt`
* `ai_interactions.md`

The generated changes included:

* Five additional song attributes
* Numeric conversion logic for the new CSV fields
* Advanced similarity scoring
* Genre-First, Mood-First, and Energy-Focused modes
* An artist repetition penalty
* A greedy recommendation-selection process
* Tabular terminal output using `tabulate`

### What did I verify or fix manually?

I manually checked that every CSV row had the same number of columns. I also fixed a `KeyError` that happened when the loader expected new fields before the CSV was fully updated.

I ran the recommender with four user profiles and compared the rankings. I also noticed that the first diversity implementation only penalized songs after the original top results had already been selected. I changed the logic so candidate scores are recalculated during every selection round.

I ran:

```bash
pytest
python3 -m src.main
```

after major changes and confirmed that all tests passed and the CLI output remained readable.

---

## Design Pattern

### Which design pattern did I use?

I used a simplified **Strategy-style pattern**.

Instead of creating separate classes for every strategy, the recommender accepts a `mode` parameter. The selected mode changes the weights used by the same shared scoring and ranking functions.

### How did AI help brainstorm or implement it?

AI suggested separating the choice of scoring weights from the rest of the algorithm. This made it possible to reuse the same code while changing the recommendation behavior.

The suggested modes were:

* Genre-First
* Mood-First
* Energy-Focused

### How does the pattern appear in the final code?

The pattern appears in the `mode` parameter used by `score_song()` and `recommend_songs()` in `src/recommender.py`.

The supported values are:

```python
"genre"
"mood"
"energy"
```

Each value selects a different set of genre and mood weights while reusing the same scoring function.

---

## Optional Challenge 1: Advanced Song Features

### Prompt Used

I asked AI to generate realistic values for five new song attributes: popularity, release decade, instrumentalness, liveness, and speechiness. The values had to match the existing 18 songs and use valid numeric ranges.

### AI-Generated Changes

The dataset was expanded with five new columns:

* `popularity`
* `release_decade`
* `instrumentalness`
* `liveness`
* `speechiness`

The CSV loader was updated to convert the new numeric values into integers or floats. The scoring function was updated so each new feature contributes to the final recommendation score.

### Manual Verification

I checked the CSV header and several rows to make sure every song had the same number of columns. I ran the recommender with four user profiles and confirmed that the new attributes changed the rankings.

The conflicting calm workout profile began favoring popular, recent, low-speech songs even when they did not match the requested genre or mood. This showed that adding many equally weighted features can overwhelm the original preferences.

I also ran `pytest`, and all tests passed.

---

## Optional Challenge 2: Multiple Scoring Modes

### Prompt Used

I asked AI to help me design multiple scoring modes while keeping the code modular. I wanted users to switch between Genre-First, Mood-First, and Energy-Focused strategies without duplicating the entire recommendation algorithm.

### AI-Suggested Design

AI suggested adding a `mode` parameter to `score_song()` and `recommend_songs()`.

The modes use these weights:

* Genre-First: genre = 3.0, mood = 2.0
* Mood-First: genre = 2.0, mood = 3.0
* Energy-Focused: genre = 1.0, mood = 1.0

The same scoring and ranking functions are reused, which keeps the code modular and avoids duplicate logic.

### Manual Verification

I ran the recommender using the Energy-Focused mode with four user profiles. The output changed because genre and mood had less influence relative to the numerical features.

For example, `Gym Hero` ranked above `Aftermath Echo` for the Deep Intense Rock profile because its energy and other numeric attributes were closer to the target values.

I also ran `pytest`, and all tests passed.

---

## Optional Challenge 3: Diversity and Fairness Logic

### Prompt Used

I asked AI to help me add a diversity penalty to the recommender. If an artist was already represented in the selected recommendations, later songs by that artist would receive a score penalty.

I also asked that the remaining candidate scores be recalculated after every selection so another artist could move up when appropriate.

### AI-Suggested Design

AI suggested selecting recommendations one at a time.

Before each selection:

1. Recalculate the adjusted score of every remaining song.
2. Apply a `0.5` penalty to songs by artists already selected.
3. Choose the highest adjusted score.
4. Remove the selected song from the remaining candidates.
5. Repeat until the top `k` recommendations are chosen.

### Manual Verification

I tested the diversity logic using the Chill Lofi profile.

`Midnight Coding` and `Focus Flow` are both by LoRoom, so `Focus Flow` received a repeated-artist penalty of `0.5` points after `Midnight Coding` had already been selected.

It still remained in the top five because its adjusted score was high enough. I confirmed that the explanation displayed the penalty and that all tests passed.

---

## Optional Challenge 4: Visual Summary Table

### Prompt Used

I asked AI to suggest a readable terminal format that would show the song title, final score, and scoring reasons in one place.

### AI-Suggested Design

AI suggested using the `tabulate` library.

The CLI builds a list of recommendation rows and passes them to:

```python
tabulate(
    table,
    headers=["Song", "Score", "Reasons"],
    tablefmt="grid",
)
```

### Manual Verification

I installed `tabulate`, added it to `requirements.txt`, and ran the application.

The terminal output displayed each profile's top recommendations in a readable table with columns for:

* Song
* Score
* Reasons

I also confirmed that the explanations included score contributions and diversity penalties where applicable.
