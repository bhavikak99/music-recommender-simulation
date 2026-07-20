import csv
from typing import List, Dict, Tuple
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def score_song_object(self, user: UserProfile, song: Song) -> float:
        score = 0.0

        if song.genre == user.favorite_genre:
            score += 3.0

        if song.mood == user.favorite_mood:
            score += 2.0

        score += 1 - abs(song.energy - user.target_energy)

        if user.likes_acoustic and song.acousticness >= 0.5:
            score += 1.0
        elif not user.likes_acoustic and song.acousticness < 0.5:
            score += 1.0

        return score

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored_songs = []

        for song in self.songs:
            score = self.score_song_object(user, song)
            scored_songs.append((song, score))

        scored_songs.sort(key=lambda item: item[1], reverse=True)

        return [song for song, score in scored_songs[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []

        if song.genre == user.favorite_genre:
            reasons.append(f"matches your favorite genre: {user.favorite_genre}")

        if song.mood == user.favorite_mood:
            reasons.append(f"matches your favorite mood: {user.favorite_mood}")

        energy_similarity = 1 - abs(song.energy - user.target_energy)
        reasons.append(f"has energy close to your target ({energy_similarity:.2f} similarity)")

        if user.likes_acoustic and song.acousticness >= 0.5:
            reasons.append("matches your preference for acoustic songs")
        elif not user.likes_acoustic and song.acousticness < 0.5:
            reasons.append("matches your preference for less acoustic songs")

        return "; ".join(reasons)

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    songs = []

    with open(csv_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            row["popularity"] = int(row["popularity"])
            row["instrumentalness"] = float(row["instrumentalness"])
            row["liveness"] = float(row["liveness"])
            row["speechiness"] = float(row["speechiness"])

            songs.append(row)

    return songs

def score_song(user_prefs: Dict, song: Dict, mode: str = "genre") -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    score = 0.0
    reasons = []

    if mode == "genre":
        genre_points = 3.0
        mood_points = 2.0
    elif mode == "mood":
        genre_points = 2.0
        mood_points = 3.0
    elif mode == "energy":
        genre_points = 1.0
        mood_points = 1.0
    else:
        genre_points = 3.0
        mood_points = 2.0

    if song["genre"] == user_prefs["genre"]:
        score += genre_points
        reasons.append(f"genre match (+{genre_points:.1f})")

    if song["mood"] == user_prefs["mood"]:
        score += mood_points
        reasons.append(f"mood match (+{mood_points:.1f})")

    energy_similarity = 1 - abs(song["energy"] - user_prefs["energy"])
    score += energy_similarity
    reasons.append(f"energy similarity (+{energy_similarity:.2f})")

    popularity_similarity = 1 - abs(
        song["popularity"] - user_prefs["target_popularity"]
    ) / 100
    score += popularity_similarity
    reasons.append(
        f"popularity similarity (+{popularity_similarity:.2f})"
    )

    if song["release_decade"] == user_prefs["preferred_release_decade"]:
        score += 1.0
        reasons.append("release decade match (+1.0)")

    instrumentalness_similarity = 1 - abs(
        song["instrumentalness"] - user_prefs["target_instrumentalness"]
    )
    score += instrumentalness_similarity
    reasons.append(
        f"instrumentalness similarity (+{instrumentalness_similarity:.2f})"
    )

    liveness_similarity = 1 - abs(
        song["liveness"] - user_prefs["target_liveness"]
    )
    score += liveness_similarity
    reasons.append(
        f"liveness similarity (+{liveness_similarity:.2f})"
    )

    speechiness_similarity = 1 - abs(
        song["speechiness"] - user_prefs["target_speechiness"]
    )
    score += speechiness_similarity
    reasons.append(
        f"speechiness similarity (+{speechiness_similarity:.2f})"
    )

    return score, reasons

def recommend_songs(
    user_prefs: Dict,
    songs: List[Dict],
    k: int = 5,
    mode: str = "genre",
    diversity_penalty: float = 0.5,
) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    scored_songs = []

    for song in songs:
        score, reasons = score_song(user_prefs, song, mode)
        explanation = ", ".join(reasons)
        scored_songs.append((song, score, explanation))

    scored_songs.sort(key=lambda item: item[1], reverse=True)

    recommendations = []
    selected_artists = set()
    remaining_songs = scored_songs.copy()

    while remaining_songs and len(recommendations) < k:
        adjusted_candidates = []

        for song, score, explanation in remaining_songs:
            adjusted_score = score
            adjusted_explanation = explanation

            if song["artist"] in selected_artists:
                adjusted_score -= diversity_penalty
                adjusted_explanation += (
                    f", repeated artist penalty (-{diversity_penalty:.1f})"
                )

            adjusted_candidates.append(
                (song, adjusted_score, adjusted_explanation)
            )

        best_song, best_score, best_explanation = max(
            adjusted_candidates,
            key=lambda item: item[1],
        )

        recommendations.append(
            (best_song, best_score, best_explanation)
        )
        selected_artists.add(best_song["artist"])

        remaining_songs = [
            item for item in remaining_songs
            if item[0]["id"] != best_song["id"]
        ]

    return recommendations