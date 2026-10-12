# 🍉 Fruit Slicing Game Using OpenCV and MediaPipe

A real-time computer vision based fruit slicing game built using **Python, OpenCV, MediaPipe, and Pygame**.

The player controls a virtual knife using their **index finger** detected through a webcam. Fruits appear on the screen and can be sliced by moving the finger across them. Bombs must be avoided because slicing a bomb costs a life.

---

## 🎮 Game Features

- 🖐️ Real-time hand tracking using MediaPipe
- 📷 Webcam-based gameplay
- 🍎 Multiple fruit types
- 💣 Bomb obstacles
- 🔪 Finger-controlled slicing
- ✨ Knife trail effect
- 💥 Particle effects
- ❤️ Three-life system
- ⏱️ 60-second game timer
- 🏆 High-score system
- 🔊 Sound effects
- 🎵 Start, slicing, bomb, timer, and game-over sounds
- 🎮 Keyboard and mouse controls
- 🖥️ Start menu
- 🏁 Game-over screen
- 🔄 Play-again functionality

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Main programming language |
| OpenCV | Webcam capture and game rendering |
| MediaPipe | Real-time hand and finger tracking |
| Pygame | Sound effects |
| NumPy | Graphics and particle calculations |
| Git | Version control |
| GitHub | Project hosting |

---

## 📁 Project Structure

```text
Fruit_Slicing_Game/
│
├── assets/
│   └── sounds/
│       ├── bomb.wav
│       ├── game_over.wav
│       ├── slice.wav
│       ├── start.wav
│       └── tick.wav
│
├── models/
│   └── hand_landmarker.task
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── hand_tracker.py
│   ├── fruit.py
│   ├── game.py
│   └── settings.py
│
├── tests/
│
├── create_sounds.py
├── high_score.txt
├── requirements.txt
├── README.md
└── .gitignore

1. Create a virtual environment

Windows PowerShell:

python -m venv .venv

Activate it:

.\.venv\Scripts\Activate.ps1

2. Install dependencies

pip install -r requirements.txt

3. Verify the MediaPipe model

The project requires the MediaPipe Hand Landmarker model:

models/hand_landmarker.task

Make sure this file exists before running the game.

▶️ How to Run

From the project root directory, run:

python .\src\main.py

The webcam will open and the game menu will appear.

Press ENTER or click PLAY to start the game.

🎮 Controls

Control	Action
Index finger	Slice fruits
ENTER	Start / restart game
R	Restart after game over
Q	Quit game
Mouse click	Select menu buttons

🍎 How to Play

Start the game.
Position your hand in front of the webcam.
The MediaPipe hand tracker detects your hand.
Your index fingertip acts as the virtual knife.
Move your finger across fruits to slice them.
Avoid bombs.
Slicing fruits increases your score.
Slicing a bomb removes one life.
The game lasts for 60 seconds.
Your highest score is saved in high_score.txt.

❤️ Lives

The player starts with 3 lives.

Each time a bomb is sliced:

❤️ → ❤️ → 💔

When all lives are lost, the game ends.

🏆 High Score

The game automatically saves the highest score in:

high_score.txt

The high score is loaded when the game starts and updated whenever a new high score is achieved.

🔊 Sound Effects

The game includes several sound effects:

start.wav — game start
slice.wav — fruit slicing
bomb.wav — bomb sliced
tick.wav — timer warning
game_over.wav — game over

All sound files are stored inside:

assets/sounds/

🖐️ Hand Tracking

The project uses the MediaPipe Hand Landmarker to detect the player's hand through the webcam.

The index fingertip position is used as the slicing point.

The tracking pipeline is:

Webcam
   ↓
OpenCV
   ↓
MediaPipe Hand Landmarker
   ↓
Hand Detection
   ↓
Index Fingertip Position
   ↓
Virtual Knife
   ↓
Fruit Collision Detection
   ↓
Score / Lives

🎯 Game Flow

Start Menu
    │
    ▼
Press ENTER / PLAY
    │
    ▼
Gameplay
    │
    ├── Slice Fruit → Increase Score
    │
    ├── Slice Bomb → Lose Life
    │
    └── Timer / Lives End
             │
             ▼
        Game Over
             │
       ┌─────┴─────┐
       ▼           ▼
   Play Again      Quit

📦 Main Components
main.py

Controls the main application loop, webcam input, game states, hand tracking, keyboard/mouse input, and rendering.

hand_tracker.py

Handles MediaPipe Hand Landmarker initialization and hand detection.

fruit.py

Defines fruit objects, movement, drawing, slicing detection, and sliced-fruit animation.

game.py

Controls:

Fruit spawning
Bomb spawning
Score
Lives
Timer
Collision detection
Particles
High score
Game-over state
settings.py

Stores project configuration and settings.

create_sounds.py

Used to generate the game's sound files.

🧪 Testing

Before running the game, verify:

Webcam is connected.
models/hand_landmarker.task exists.
Sound files exist.
Python environment is activated.
Required packages are installed.

Run:

python .\src\main.py
🚀 Future Improvements

Possible future improvements include:

More fruit types
Different difficulty levels
Improved visual effects
Additional game modes
Better animations
Online leaderboard
Mobile or web version

👨‍💻 Project

Fruit Slicing Game Using OpenCV and MediaPipe

Built as a computer vision project demonstrating real-time hand tracking and interactive gameplay.

📄 License

This project is intended for educational and demonstration purposes.


---

# 4. Save the README

In VS Code:

```text
Ctrl + S