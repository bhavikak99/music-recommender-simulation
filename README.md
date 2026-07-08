# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## How The System Works

Real-world music platforms use user behavior and song information to predict what someone might enjoy next. For example, collaborative filtering looks at patterns from many users, such as likes, skips, playlists, and repeat listens, while content-based filtering looks at the features of songs themselves, such as genre, mood, tempo, and energy. My simulator will focus on a simple content-based approach: it compares a user's taste profile to each song's attributes and gives higher scores to songs that are closer matches.

Each `Song` in my system will use these features:

- `genre`
- `mood`
- `energy`
- `valence`
- `danceability`
- `acousticness`
- `tempo_bpm`

Each `UserProfile` stores the user's preferred genre, mood, energy level, valence, danceability, acousticness, and tempo. The recommender starts each song with a score of 0. It awards **3 points** for a matching genre and **2 points** for a matching mood. For the numerical features (energy, valence, danceability, acousticness, and tempo), it gives higher similarity scores to songs whose values are closer to the user's preferred values. After every song has been scored, the recommender sorts the songs from highest score to lowest score and recommends the top matches.

Because genre has the highest weight, this recommender may favor songs with the correct genre even if songs from other genres have very similar moods or audio characteristics. This could create a bias toward certain genres and reduce the variety of recommendations.

These features are useful because genre and mood describe the overall style or vibe of a song, while energy, valence, danceability, acousticness, and tempo give more detailed numeric information. For example, two songs can both be pop, but one might be calm and acoustic while another is fast, energetic, and danceable.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:

```
# e.g.:
# User profile: genre=indie, mood=chill, energy=low
# Recommendations:
#   1. ...
#   2. ...
#   3. ...
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



