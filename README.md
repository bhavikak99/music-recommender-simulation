# Music Recommender Simulation

## Project Summary

This project implements a simple content-based music recommender in Python. It loads songs from a CSV file, compares each song's genre, mood, and energy to a user's preferences, assigns a weighted score based on how closely the song matches, and ranks the songs from highest to lowest score. The program then displays the top recommendations along with an explanation of why each song was selected.

---

## How The System Works

Real-world music platforms use user behavior and song information to predict what someone might enjoy next. For example, collaborative filtering looks at patterns from many users, such as likes, skips, playlists, and repeat listens, while content-based filtering looks at the features of songs themselves, such as genre, mood, tempo, and energy. My simulator focuses on a simple content-based approach by comparing a user's preferences with each song's attributes and assigning a score based on how well they match.

Each `Song` in my system uses these features:

* `genre`
* `mood`
* `energy`
* `valence`
* `danceability`
* `acousticness`
* `tempo_bpm`

The current recommendation algorithm uses:

* Genre
* Mood
* Energy

Each `UserProfile` stores the user's preferred genre, preferred mood, and target energy level.

### Algorithm Recipe

For every song:

* Start with a score of **0**.
* Add **3.0 points** if the song's genre matches the user's favorite genre.
* Add **2.0 points** if the song's mood matches the user's favorite mood.
* Add an **energy similarity score** using:

  ```
  similarity = 1 - abs(song_energy - target_energy)
  ```

After every song has been scored, the recommender sorts the songs from highest score to lowest score and returns the top recommendations.

### Potential Biases

Because genre receives the highest weight, this recommender may over-prioritize songs from the preferred genre even when songs from other genres have very similar moods or energy levels. Since it only considers a few song attributes, it also cannot account for lyrics, artist preferences, or listening history, which may reduce recommendation diversity.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate      # Mac or Linux
.venv\Scripts\activate         # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python3 -m src.main
```

### Running Tests

Run the tests with:

```bash
pytest
```

---

## Sample Recommendation Output

```text
Top recommendations:

Club Gravity - Score: 6.00
Because: genre match (+3.0), mood match (+2.0), energy similarity (+1.00)

Pixel Rush - Score: 2.93
Because: mood match (+2.0), energy similarity (+0.93)

Gym Hero - Score: 0.98
Because: energy similarity (+0.98)

Storm Runner - Score: 0.96
Because: energy similarity (+0.96)

Sunrise City - Score: 0.87
Because: energy similarity (+0.87)
```

**Screenshot or video (optional):** Add a screenshot of the terminal output if desired.

---

## Experiments You Tried

* Increased the genre weight to **3.0** so that genre became the strongest recommendation factor.
* Used an energetic dance user profile to verify that energetic dance songs ranked higher than calmer songs.
* Tested the recommender with both the starter **pop/happy** profile and the custom **dance/energetic** profile to observe how the rankings changed.

---

## Limitations and Risks

* The recommender only works with a small catalog of songs.
* It only considers genre, mood, and energy when calculating recommendations.
* It does not understand lyrics, artists, listening history, or user behavior.
* It may over-favor one genre because genre has the largest weight.
* It can create a limited "filter bubble" by repeatedly recommending songs that are very similar.

---

## Reflection

This project helped me understand how recommendation systems transform data into predictions. By comparing a user's preferences with song attributes and assigning weighted scores, the recommender can rank songs according to how closely they match the user's taste. I also learned why scoring individual songs and then ranking the results are two separate steps in the recommendation process.

I also learned that simple recommendation systems can introduce bias. Since my recommender gives the most weight to genre, it may repeatedly recommend songs from the same genre while ignoring songs that have similar moods or energy. Real-world recommendation systems face similar challenges and often combine multiple recommendation techniques to provide more diverse and personalized suggestions.
