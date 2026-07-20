# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**BeatMatch Recommender 1.0**

---

## 2. Intended Use

This recommender is designed to recommend songs based on a user's music preferences using a simple content-based recommendation approach. It compares song features such as genre, mood, and energy to the user's preferred values and ranks the songs from best to worst match.

This model assumes that a user's favorite genre, mood, and energy level are good indicators of what they will enjoy. It was created as a classroom project to demonstrate how recommendation systems work rather than for real-world production use.

---

## 3. How the Model Works

Each song contains descriptive features such as genre, mood, energy, tempo, danceability, valence, and acousticness. The current recommendation algorithm uses genre, mood, and energy to calculate a score.

The model begins with a score of zero for every song. It awards 3 points when the song's genre matches the user's preferred genre and 2 points when the mood matches. It then calculates an energy similarity score by comparing the song's energy level to the user's preferred energy level. Songs with higher total scores are ranked first and recommended to the user.

Compared to the starter project, I implemented a weighted scoring system that explains why each recommendation was selected.

---

## 4. Data

The recommender uses a CSV dataset containing 18 songs. The dataset includes a variety of genres such as pop, rock, lofi, jazz, ambient, folk, dance, electronic, synthwave, and chiptune. It also includes moods like happy, energetic, relaxed, chill, focused, moody, peaceful, and intense.

I expanded the original dataset by adding additional songs to increase genre and mood diversity.

Although the dataset includes several useful numerical features, it is still very small and does not include information such as lyrics, release year, popularity, or listening history.

---

## 5. Strengths

The recommender performs well when the user's preferences clearly match songs in the dataset. For example, the dance and energetic user profile correctly ranked **Club Gravity** as the highest recommendation because it matched the user's preferred genre, mood, and energy level.

The weighted scoring system is easy to understand, and the recommendation explanations help users see why each song received its score.

---

## 6. Limitations and Bias

This recommender only considers genre, mood, and energy when calculating recommendations. It ignores many factors that influence music preferences, including artists, lyrics, listening history, playlists, and popularity.

Because genre receives the highest weight, the recommender may repeatedly recommend songs from the same genre even if songs from other genres have similar moods or energy. This could create a filter bubble and reduce recommendation diversity.

---

## 7. Evaluation

I tested the recommender using both the starter pop/happy profile and my custom dance/energetic profile.

For the dance profile, the recommender ranked **Club Gravity** first, followed by other energetic songs such as **Pixel Rush** and **Gym Hero**. These recommendations matched my expectations because they closely matched the user's preferences.

I also verified that the project passed all provided pytest tests and that the command-line application produced readable recommendation explanations.

---

## 8. Future Work

If I continued developing this project, I would include additional song features such as valence, danceability, acousticness, and tempo in the scoring algorithm. I would also allow users to assign their own weights to different features.

Another improvement would be combining content-based recommendations with collaborative filtering so the recommender could learn from the listening behavior of similar users while still considering song characteristics.

---

## 9. Personal Reflection

This project helped me understand how recommendation systems transform user preferences into predictions using weighted scoring. I learned that recommendation systems are not simply matching genres but instead compare multiple features and rank every item before making suggestions.

I also realized that even simple recommendation systems can introduce bias depending on how the scoring algorithm is designed. Small decisions, such as giving genre a higher weight than mood, can significantly influence which songs users see and which songs they never discover.
