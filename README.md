# 🎵 Music Recommender Simulation

## Project Summary

This project implements a content-based music recommender in Python. It loads songs from a CSV file, compares each song's attributes with a user's preferences, calculates a weighted score, and ranks the songs from highest to lowest score.

The recommender supports multiple ranking modes, advanced song attributes, recommendation explanations, an artist diversity penalty, and formatted terminal tables.

---

## How The System Works

Real-world music platforms use user behavior and song information to predict what someone might enjoy next.

**Collaborative filtering** uses patterns from many users, such as likes, skips, playlists, repeat listens, and shared listening behavior.

**Content-based filtering** compares the attributes of songs with the preferences of one user. These attributes may include genre, mood, energy, tempo, and other audio characteristics.

This simulator uses a content-based approach.

### Song Features

Each song includes:

* `genre`
* `mood`
* `energy`
* `tempo_bpm`
* `valence`
* `danceability`
* `acousticness`
* `popularity`
* `release_decade`
* `instrumentalness`
* `liveness`
* `speechiness`

The CSV contains 18 songs.

### User Preferences

Each user profile includes preferences such as:

* Preferred genre
* Preferred mood
* Target energy
* Target popularity
* Preferred release decade
* Target instrumentalness
* Target liveness
* Target speechiness

### Algorithm Recipe

For every song, the recommender:

1. Starts the score at `0`.
2. Adds points for matching genre.
3. Adds points for matching mood.
4. Calculates energy similarity.
5. Calculates popularity similarity.
6. Adds a point for a matching release decade.
7. Calculates instrumentalness similarity.
8. Calculates liveness similarity.
9. Calculates speechiness similarity.
10. Adds the song to a ranked list based on its total score.

A numerical similarity uses the difference between a song's value and the user's preferred value. Smaller differences produce higher similarity scores.

For example:

```text
energy similarity = 1 - absolute difference
```

### Ranking Modes

The recommender supports three scoring modes:

* **Genre-First:** Genre has the highest categorical weight.
* **Mood-First:** Mood has the highest categorical weight.
* **Energy-Focused:** Genre and mood have smaller weights, so numerical features have more influence.

The mode can be changed in `src/main.py`:

```python
mode="genre"
mode="mood"
mode="energy"
```

### Diversity Logic

The recommender applies a repeated-artist penalty during selection.

When a song by an artist has already been selected, later songs by the same artist receive a `0.5` point penalty. The program recalculates candidate scores before selecting each recommendation.

This helps other artists appear in the results and reduces repetition.

### Recommendation Explanations

Every recommendation includes reasons such as:

```text
genre match (+1.0)
mood match (+1.0)
energy similarity (+0.92)
popularity similarity (+0.92)
release decade match (+1.0)
repeated artist penalty (-0.5)
```

---

## Getting Started

### Setup

1. Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
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

```bash
pytest
```

---

## Sample Recommendation Output

The terminal uses `tabulate` to display recommendations in a readable table.

```text
Profile: High-Energy Pop | Mode: Energy-Focused

+----------------+-------+--------------------------------------------------+
| Song           | Score | Reasons                                          |
+----------------+-------+--------------------------------------------------+
| Sunrise City   | 7.72  | genre match, mood match, feature similarities    |
| Rooftop Lights | 6.71  | mood match and strong numerical similarities     |
| Gym Hero       | 6.65  | genre match and strong numerical similarities    |
+----------------+-------+--------------------------------------------------+
```

The full program displays the exact point contribution for every scoring reason.

---

## Evaluation Profiles

The recommender was tested with four profiles.

### High-Energy Pop

```text
Preferred genre: pop
Preferred mood: happy
Target energy: 0.90
```

This profile favored upbeat, popular, recent songs. *Sunrise City* ranked first because it matched genre and mood and had strong numerical similarities.

### Chill Lofi

```text
Preferred genre: lofi
Preferred mood: chill
Target energy: 0.35
```

This profile favored *Midnight Coding* and *Library Rain*. *Focus Flow* received a repeated-artist penalty because another LoRoom song had already been selected.

### Deep Intense Rock

```text
Preferred genre: rock
Preferred mood: intense
Target energy: 0.90
```

This profile ranked *Storm Runner* highly because it matched genre, mood, and energy.

### Conflicting Calm Workout

```text
Preferred genre: ambient
Preferred mood: relaxed
Target energy: 0.95
```

This edge-case profile combined calm categories with high energy. It showed that multiple advanced feature similarities could sometimes outweigh genre and mood.

---

## Experiments

### Weight-Shift Experiment

I reduced the genre weight and increased the relative importance of energy. This caused high-energy songs to move higher in several rankings.

### Multiple Scoring Modes

I created Genre-First, Mood-First, and Energy-Focused ranking modes. The same scoring function is reused with different weights.

### Diversity Experiment

I added an artist penalty. When the same artist appears more than once, later songs by that artist receive a score reduction.

### Advanced Feature Experiment

I added:

* Popularity
* Release decade
* Instrumentalness
* Liveness
* Speechiness

These features changed the rankings significantly. They also showed that adding many equally weighted features can overpower the original genre and mood preferences.

---

## Limitations and Risks

* The dataset contains only 18 fictional songs.
* The recommender does not learn from real listening behavior.
* It does not understand lyrics or personal memories connected to music.
* Advanced features may overpower genre and mood.
* The same fixed preferences are currently used for several advanced features.
* The artist penalty reduces repetition but does not guarantee complete diversity.
* Some genres and moods are underrepresented.
* The recommender can still create a filter bubble by repeatedly selecting songs with similar attributes.

---

## Reflection

This project helped me understand the difference between input data, user preferences, scoring, and ranking.

The song dataset is the input. The user profile describes the target preferences. The scoring function compares each song with those preferences. The ranking function sorts the results and returns the best matches.

I also learned that a recommendation system can feel intelligent even when it uses simple rules. However, its behavior depends heavily on the features and weights chosen by the developer. Adding more features made the system more detailed, but it also introduced new problems because some features became too influential.

AI helped with brainstorming, generating advanced song values, explaining design ideas, and debugging. I still needed to manually verify the CSV, inspect the scoring math, run tests, and correct logic that did not behave as intended.

For future work, I would allow users to choose their own feature weights, add real listening data, improve genre diversity, and create automated tests for every scoring mode.
