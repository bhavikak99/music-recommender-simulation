from typing import List, Dict, Tuple, Optional
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
    # TODO: Implement CSV loading logic
    print(f"Loading songs from {csv_path}...")
    return []

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """
    Scores a single song against user preferences.
    Required by recommend_songs() and src/main.py
    """
    # TODO: Implement scoring logic using your Algorithm Recipe from Phase 2.
    # Expected return format: (score, reasons)
    return []

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    # TODO: Implement scoring and ranking logic
    # Expected return format: (song_dict, score, explanation)
    return []
