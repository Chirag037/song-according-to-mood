import tkinter as tk
import webbrowser
import random

# Sample mood-song mapping
mood_songs = {
    "Happy": [
        "https://youtu.be/ZbZSe6N_BXs",
        "https://youtu.be/d-diB65scQU",
        "https://youtu.be/y6Sxv-sUYtM"
    ],
    "Sad": [
        "https://youtu.be/Ho32Oh6b4jc",  # Lewis Capaldi – Someone You Loved
        "https://youtu.be/JGwWNGJdvx8",  # Ed Sheeran – Shape of You (emotional version)
        "https://youtu.be/8UVNT4wvIGY"   # Gotye – Somebody That I Used to Know
    ],

    "Angry": [
            "https://youtu.be/X0pH2b7vS8A",
            "https://youtu.be/04F4xlWSFh0",
            "https://youtu.be/ZpUYjpKg9KY"
     ],
      
    "Relaxed": [
        "https://youtu.be/2OEL4P1Rz04",
        "https://youtu.be/1ZYbU82GVz4",
        "https://youtu.be/MkNeIUgNPQ8"
    ]
}

# Function to recommend and open a song

def recommend_song(mood):
    if mood in mood_songs:
        url = random.choice(mood_songs[mood])
        webbrowser.open(url)
    else:
        print("Mood not found")

# GUI setup
root = tk.Tk()
root.title("Mood-Based Music Recommender")
root.geometry("400x300")
root.configure(bg="#222222")

# Heading
heading = tk.Label(root, text="How are you feeling today?", font=("Helvetica", 16), bg="#222222", fg="white")
heading.pack(pady=20)

# Button creator
def create_button(mood):
    return tk.Button(
        root, 
        text=mood, 
        font=("Helvetica", 12), 
        width=15, 
        bg="#444444", 
        fg="white", 
        command=lambda: recommend_song(mood)
    )

# Mood buttons
moods = ["Happy", "Sad", "Angry", "Relaxed"]
for mood in moods:
    btn = create_button(mood)
    btn.pack(pady=5)

# Run the app
root.mainloop()
