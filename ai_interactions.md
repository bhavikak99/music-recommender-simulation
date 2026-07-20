# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agentic Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

<!-- Describe the goal you asked the agent to accomplish -->

**Prompts used:**

<!-- Paste the key prompts you gave the agent -->

**What did the agent generate or change?**

<!-- List the files edited, code generated, or commands run -->

**What did you verify or fix manually?**

<!-- Describe anything the agent got wrong or that required human review -->

---

## Design Pattern (SF10)

> Document how AI helped you choose or implement a design pattern.

**Which design pattern did you use?**

<!-- e.g., Strategy, Factory, Observer, etc. -->

**How did AI help you brainstorm or implement it?**

<!-- Describe the conversation or suggestions that led to your decision -->

**How does the pattern appear in your final code?**

<!-- Point to the relevant class or method -->

## Optional Challenge 1: Advanced Song Features

### Prompt Used

I asked AI to generate realistic values for five new song attributes: popularity, release decade, instrumentalness, liveness, and speechiness. The values had to match the existing 18 songs and use valid numeric ranges.

### AI-Generated Changes

The dataset was expanded with five new columns:

- popularity
- release_decade
- instrumentalness
- liveness
- speechiness

The CSV loader was updated to convert the new numeric values into integers or floats. The scoring function was also updated so each new feature contributes to the final recommendation score.

### Manual Verification

I checked the CSV header and several rows to make sure every song had the same number of columns. I ran the recommender with four user profiles and confirmed that the new attributes changed the rankings. For example, the conflicting calm workout profile began favoring popular, recent, low-speech songs even when they did not match the requested genre or mood. This showed that adding many equally weighted features can overwhelm the original preferences. I also ran `pytest`, and all tests passed.

## Optional Challenge 2: Multiple Scoring Modes

### Prompt Used

Help me design multiple scoring modes for my music recommender while keeping the code modular. I want users to switch between Genre-First, Mood-First, and Energy-Focused strategies without duplicating the whole recommendation algorithm.

### AI-Suggested Design

The AI suggested adding a `mode` parameter to `score_song()` and `recommend_songs()`. Each mode changes the weights used for genre and mood:

- Genre-First: genre = 3.0, mood = 2.0
- Mood-First: genre = 2.0, mood = 3.0
- Energy-Focused: genre = 1.0, mood = 1.0

The same scoring and ranking functions are reused, which keeps the design modular and avoids duplicate code.

### Manual Verification

I ran the recommender using the Energy-Focused mode with four user profiles. The output changed because genre and mood had less influence relative to energy. For example, Gym Hero ranked above Aftermath Echo for the Deep Intense Rock profile because its energy was closer to the target. I also ran `pytest`, and all tests passed.

## Optional Challenge 3: Diversity and Fairness Logic

### Prompt Used

Help me add a diversity penalty to my music recommender. If an artist is already represented in the selected recommendations, reduce the score of additional songs by that artist. The selection should be recalculated after every recommendation so another song can replace a repeated artist when appropriate.

### AI-Suggested Design

The AI suggested selecting recommendations one at a time. Before each selection, the algorithm recalculates the adjusted scores of the remaining songs. Songs by an artist already included in the recommendation list receive a 0.5-point penalty.

This greedy selection process allows songs outside the original top five to move up when repeated artists are penalized.

### Manual Verification

I tested the diversity logic using the Chill Lofi profile. Midnight Coding and Focus Flow are both by LoRoom, so Focus Flow received a repeated-artist penalty of 0.5 points. It remained in the top five because its adjusted score was still high enough. I confirmed that the explanation displayed the penalty and that all pytest tests passed.