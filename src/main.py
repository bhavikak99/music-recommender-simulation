"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from tabulate import tabulate
from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv")

    profiles = {
        "High-Energy Pop": {
            "genre": "pop",
            "mood": "happy",
            "energy": 0.90,
        },
        "Chill Lofi": {
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.35,
        },
        "Deep Intense Rock": {
            "genre": "rock",
            "mood": "intense",
            "energy": 0.90,
        },
        "Conflicting Calm Workout": {
            "genre": "ambient",
            "mood": "relaxed",
            "energy": 0.95,
        },
    }

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(
            user_prefs,
            songs,
            k=5,
            mode="energy",
        )

        print(f"\nProfile: {profile_name} | Mode: Energy-Focused")
        print("Top recommendations:\n")

        table = []

        for song, score, explanation in recommendations:
            table.append([
                song["title"],
                f"{score:.2f}",
                explanation
            ])

        print(
            tabulate(
                table,
                headers=["Song", "Score", "Reasons"],
                tablefmt="grid"
            )
        )

if __name__ == "__main__":
    main()
