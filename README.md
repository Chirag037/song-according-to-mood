Mood-Based Music Recommender 🎵

A simple and fun Python application that recommends music based on your current mood using a graphical interface built with Tkinter.

🧠 How It Works

The app asks how you're feeling (Happy, Sad, Angry, Relaxed).

Based on your mood, it randomly selects a song from a curated YouTube playlist.

The selected song is then opened in your default web browser.

🛠 Features

Easy-to-use GUI built with Tkinter

Randomized music recommendation

Expandable mood and music database

📂 File Structure

MoodMusicRecommender/
├── mood_music_recommender.py   # Main Python app
├── README.md                   # Project documentation

📦 Requirements

Python 3.x

You don't need to install any external libraries. Tkinter and webbrowser are built-in.

▶️ How to Run

Clone or download this repository.

Open a terminal in the project folder.

Run the app:

python mood_music_recommender.py

Click on a mood button to get a music recommendation.

🎵 Customization

Want to add your favorite songs?

Open mood_music_recommender.py

Locate the mood_songs dictionary

Add or modify URLs under each mood:

"Sad": [
    "https://youtu.be/Ho32Oh6b4jc",
    "https://youtu.be/JGwWNGJdvx8",
    "https://youtu.be/8UVNT4wvIGY"
]

💡 Future Ideas

Integrate Spotify or YouTube API for live search

Play local MP3 files

Use facial recognition or voice input for mood detection

Made with ❤️ in Python

