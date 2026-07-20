# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**BeatMatch Recommender 1.0**

---

## 2. Intended Use

This recommender is designed to recommend songs using a simple content-based recommendation approach. It compares a user's preferred genre, mood, and energy level with the attributes of each song and recommends the closest matches.

This project was created as a classroom simulation to demonstrate how recommendation systems work. It is intended for learning and experimentation rather than real-world music streaming services.

### Non-Intended Use

This recommender is not intended to provide personalized recommendations for real music streaming services. It should not be used to make important decisions or represent real user preferences because it uses a very small dataset and a simple scoring algorithm that considers only a few song features.

---

## 3. How the Model Works

Each song contains information such as genre, mood, energy, tempo, danceability, valence, and acousticness. The current recommendation algorithm focuses on genre, mood, and energy.

Every song starts with a score of zero. If the song matches the user's preferred genre, it earns additional points. If it matches the preferred mood, it earns more points. The model also compares the song's energy level to the user's preferred energy level. Songs with energy values closer to the user's preference receive a higher similarity score. After every song has been scored, the songs are sorted from highest score to lowest score and the top recommendations are returned along with an explanation of why they were selected.

Compared to the starter code, I implemented a weighted scoring system, recommendation explanations, CSV loading, and song ranking.

---

## 4. Data

The recommender uses a CSV dataset containing **18 songs**. The catalog includes genres such as pop, rock, lofi, ambient, jazz, dance, electronic, synthwave, folk, indie pop, and chiptune. The songs also include moods such as happy, chill, focused, relaxed, energetic, moody, peaceful, and intense.

I expanded the original dataset by adding eight additional songs to create more variety.

The dataset is still very small and does not include lyrics, artist popularity, listening history, release year, or user interaction data.

---

## 5. Strengths

The recommender performs well when users have clear music preferences. For example:

* The **High-Energy Pop** profile correctly recommended upbeat pop songs such as *Sunrise City*.
* The **Chill Lofi** profile recommended calm study music like *Library Rain* and *Midnight Coding*.
* The **Deep Intense Rock** profile correctly ranked *Storm Runner* first.

The weighted scoring system is simple to understand, and the recommendation explanations make it easy to see why each song was selected.

---

## 6. Limitations and Bias

This recommender only considers genre, mood, and energy when calculating recommendations. It ignores other important information such as artists, lyrics, playlists, listening history, and popularity.

One weakness I discovered during testing was that genre and mood often outweigh the energy preference. For example, the **Conflicting Calm Workout** profile requested very high energy music while also preferring ambient and relaxed songs. Even though *Ocean Breathing* had low energy, it still ranked first because it matched both the preferred genre and mood. This shows that the current scoring system can create a filter bubble by favoring category matches over other song characteristics.

---

## 7. Evaluation

I tested the recommender using four different user profiles:

* High-Energy Pop
* Chill Lofi
* Deep Intense Rock
* Conflicting Calm Workout (edge case)

The first three profiles produced recommendations that matched my expectations. Pop songs were recommended for the pop profile, lofi songs for the lofi profile, and rock songs for the rock profile.

The conflicting profile produced the most interesting result. Although the user requested very high energy music, *Ocean Breathing* still ranked first because it matched both the preferred genre and mood. This showed that the genre and mood weights currently have more influence than the energy similarity score.

I also performed a weight-shift experiment by reducing the genre weight and increasing the importance of energy. This caused high-energy songs to move higher in several recommendation lists, making the recommender more sensitive to energy differences. However, the conflicting profile still showed that matching genre and mood remained very influential.

### Profile Comparisons

* **High-Energy Pop vs. Chill Lofi:** The pop profile recommended upbeat pop songs, while the lofi profile shifted toward slower and more relaxing songs because both the preferred genre and mood changed.
* **Chill Lofi vs. Deep Intense Rock:** The recommendations changed from calm, low-energy study music to energetic rock songs because both genre and mood became much more intense.
* **Deep Intense Rock vs. Conflicting Calm Workout:** The rock profile favored energetic rock songs, while the conflicting profile selected calm ambient music despite the high energy target, demonstrating how strongly genre and mood influence the recommendations.

---

## 8. Future Work

If I continued developing this project, I would include additional song features such as tempo, valence, danceability, and acousticness in the scoring algorithm. I would also allow users to customize the importance of each feature instead of using fixed weights.

Another improvement would be combining content-based recommendations with collaborative filtering so the recommender could learn from the listening behavior of similar users while still considering song characteristics.

---

## 9. Personal Reflection

The biggest learning moment during this project was understanding how recommendation systems transform user preferences into predictions using weighted scoring and ranking. I learned that recommendation systems compare multiple song features before deciding which songs to recommend rather than simply matching genres.

AI was helpful for brainstorming scoring ideas, explaining recommendation concepts, and helping me debug my Python code. However, I still needed to verify the suggestions, test the program, and make sure the implementation matched the project requirements. One of the most interesting discoveries was seeing how small changes to the scoring weights significantly changed the recommendation results. If I continued this project, I would include additional features such as tempo, danceability, and collaborative filtering to create more accurate and diverse recommendations.

