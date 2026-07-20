# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**BeatMatch Recommender 1.0**

---

## 2. Intended Use

This recommender is designed to suggest songs using a content-based recommendation approach. It compares a user's preferences with the attributes of each song and ranks the closest matches.

The system considers genre, mood, energy, popularity, release decade, instrumentalness, liveness, and speechiness. It was created as a classroom simulation to demonstrate how recommendation systems use features, scoring, ranking, and explanations.

### Non-Intended Use

This recommender is not intended to replace a real music streaming recommendation system. It should not be used to represent real users accurately because it relies on a small, fictional dataset and a simplified scoring algorithm.

---

## 3. How the Model Works

Each song contains the following attributes:

* Genre
* Mood
* Energy
* Tempo
* Valence
* Danceability
* Acousticness
* Popularity
* Release decade
* Instrumentalness
* Liveness
* Speechiness

The current scoring function uses genre, mood, energy, popularity, release decade, instrumentalness, liveness, and speechiness.

Every song starts with a score of zero. The recommender adds points when the song's genre or mood matches the user's preferences. It also calculates similarity scores for numerical features by measuring how close each song value is to the user's target value.

The recommender supports three ranking modes:

* **Genre-First:** Genre receives more weight than mood.
* **Mood-First:** Mood receives more weight than genre.
* **Energy-Focused:** Genre and mood receive smaller weights, making numerical similarities more influential.

After all songs are scored, the recommender selects the top results. It also applies a diversity penalty when multiple songs by the same artist appear in the recommendation list. Each selected song includes a readable explanation showing how its score was calculated.

Compared with the starter code, I implemented CSV loading, numeric conversions, weighted scoring, explanations, ranking modes, advanced song features, a diversity penalty, and formatted terminal output.

---

## 4. Data

The recommender uses a CSV dataset containing **18 songs**.

The catalog includes genres such as:

* Pop
* Rock
* Lofi
* Ambient
* Jazz
* Dance
* Electronic
* Synthwave
* Folk
* Indie pop
* Chiptune

It also includes moods such as happy, chill, focused, relaxed, energetic, moody, peaceful, and intense.

I expanded the original dataset from 10 songs to 18 songs. I also added five advanced attributes:

* Popularity
* Release decade
* Instrumentalness
* Liveness
* Speechiness

The dataset is still limited because it is small and fictional. It does not contain real listening history, lyrics, playlist behavior, user ratings, or long-term preference data.

---

## 5. Strengths

The recommender works well when a user's preferences clearly match songs in the dataset.

For example:

* The **High-Energy Pop** profile favors upbeat and popular songs such as *Sunrise City*.
* The **Chill Lofi** profile favors songs such as *Midnight Coding* and *Library Rain*.
* The **Deep Intense Rock** profile ranks *Storm Runner* highly.
* The explanations show exactly which matches and similarities contributed to each score.

The multiple ranking modes also make the recommender more flexible. Users can choose whether genre, mood, or numerical similarity should have more influence.

The formatted table improves readability by displaying each song, score, and explanation in one place.

---

## 6. Limitations and Bias

The recommender uses fixed rules and cannot learn automatically from user behavior. It does not understand lyrics, cultural context, changing preferences, or why a user may like a particular artist.

The advanced attributes can also overpower the original genre and mood preferences because several numerical features each contribute similarity points. During testing, some highly popular and recent songs ranked above songs that better matched the requested genre.

The system may still create filter bubbles because matching features repeatedly favor similar songs. To reduce repetition, the recommender applies a **0.5-point artist diversity penalty** when another song by the same artist is being considered after that artist has already appeared in the recommendations. This gives other artists a better chance to appear, although it does not guarantee that every artist will be unique.

The small dataset also creates bias because some genres and moods have more matching songs than others.

---

## 7. Evaluation

I tested the recommender with four user profiles:

* High-Energy Pop
* Chill Lofi
* Deep Intense Rock
* Conflicting Calm Workout

The first three profiles generally produced results that matched my expectations. The pop profile favored upbeat songs, the lofi profile favored calmer songs, and the rock profile favored intense rock music.

The conflicting profile was designed as an edge case. It requested ambient and relaxed music with extremely high energy. Before the advanced attributes were added, *Ocean Breathing* ranked first because genre and mood matches outweighed its low energy. After the advanced attributes were included, popular and recent high-energy songs moved higher because several numerical similarities contributed to their scores.

I also ran a weight-shift experiment by reducing the genre weight and increasing the relative importance of energy. This changed the ranking order and demonstrated that small weight changes can strongly affect recommendations.

The artist diversity experiment showed that repeated artists could receive a score penalty. For the Chill Lofi profile, *Focus Flow* received a repeated-artist penalty because *Midnight Coding* by the same artist had already been selected.

### Profile Comparisons

* **High-Energy Pop vs. Chill Lofi:** The pop profile favored upbeat, popular, low-instrumental songs, while the lofi profile favored calmer and more instrumental tracks.
* **Chill Lofi vs. Deep Intense Rock:** The lofi profile preferred relaxing study music, while the rock profile shifted toward intense and energetic songs.
* **Deep Intense Rock vs. Conflicting Calm Workout:** The rock profile had consistent preferences, while the conflicting profile exposed how advanced feature similarities could outweigh genre and mood.
* **Genre-First vs. Energy-Focused:** Genre-First gives category matches more influence, while Energy-Focused makes numerical similarities more important.

## Evaluation Outputs

### High-Energy Pop

```text
Profile: High-Energy Pop | Mode: Energy-Focused

Sunrise City ranked first because it matched genre and mood and also had strong similarity scores for energy, popularity, release decade, instrumentalness, liveness, and speechiness.
```

### Chill Lofi

```text
Profile: Chill Lofi | Mode: Energy-Focused

Midnight Coding and Library Rain ranked highly because they matched the lofi and chill preferences. Focus Flow received a repeated-artist penalty because Midnight Coding by LoRoom had already been selected.
```

### Deep Intense Rock

```text
Profile: Deep Intense Rock | Mode: Energy-Focused

Storm Runner ranked first because it matched both the rock genre and intense mood while also closely matching the requested energy.
```

### Conflicting Calm Workout

```text
Profile: Conflicting Calm Workout | Mode: Energy-Focused

The profile combined ambient and relaxed preferences with very high energy. After advanced features were added, popular and recent songs such as Sunrise City and Gym Hero moved higher because multiple numerical similarities influenced the final score.
```

---

## 8. Future Work

If I continued developing this project, I would:

* Add user-specific weights for every feature.
* Normalize or reduce advanced feature weights so they do not overpower genre and mood.
* Add collaborative filtering based on user listening behavior.
* Add real song data from a larger dataset.
* Improve diversity by penalizing repeated genres as well as repeated artists.
* Let users choose their scoring mode through command-line input.
* Add more tests for scoring modes, advanced features, and diversity behavior.

---

## 9. Personal Reflection

The biggest learning moment during this project was understanding how recommendation systems transform preferences into scores and then turn those scores into a ranked list. I learned that even a simple set of weights can produce results that feel personalized.

AI helped me brainstorm scoring ideas, generate additional dataset values, understand design patterns, and debug errors. However, I still needed to inspect the code, run tests, verify CSV formatting, and make sure the final behavior matched the assignment requirements. One important example was the diversity logic. The first version applied a penalty after selecting the original top songs, so I needed to revise it so scores were recalculated during each selection round.

I was surprised by how strongly small scoring changes affected the output. Adding five advanced attributes caused some songs to rank highly even when their genre and mood did not match. This showed me that more features do not automatically make a model better; the features and their weights must be balanced carefully.

If I extended the project, I would improve the weight system, add more automated tests, and allow users to adjust preferences and ranking modes directly.
