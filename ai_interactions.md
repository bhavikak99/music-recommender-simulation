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
