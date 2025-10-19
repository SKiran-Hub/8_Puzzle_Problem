🧩 8 Puzzle Problem — AI Solver with Interactive GUI

An intelligent 8 Puzzle Problem solver built in Python using Tkinter GUI and A* (A-star) search algorithm with the Manhattan Distance heuristic.
You can interactively play, shuffle, or let the AI solve the puzzle step by step.

🎮 Features

✅ Colorful and interactive Tkinter GUI
✅ Custom initial state option — enter your own puzzle
✅ AI Solver using A* algorithm
✅ Move counter until success
✅ Real-time status updates
✅ Smooth, animated solving experience

🧠 About the 8 Puzzle Problem

The 8 Puzzle Problem is a classic AI challenge where you have a 3x3 grid containing 8 numbered tiles and one empty space.
The goal is to move tiles until the board reaches the target configuration:

1 2 3
4 5 6
7 8 _


This project implements an A* search algorithm that uses the Manhattan Distance heuristic to find the optimal sequence of moves.

🖥️ How to Run
🧩 Option 1 — Run in VS Code

Make sure you have Python 3.x installed.

Open this folder in VS Code.

In the terminal, run:

python 8_Puzzle_Problem.py


Interact with the GUI — shuffle, reset, or watch the AI solve automatically!

🧰 Option 2 — Run in Command Prompt
cd path\to\AI
python 8_Puzzle_Problem.py

🧮 Algorithm Overview

The AI uses:

A* Search Algorithm to explore states efficiently

Manhattan Distance Heuristic to estimate cost

A priority queue (min-heap) for node selection

A visited state map to avoid loops

This ensures the solver finds the shortest possible path to the goal configuration.

📸 Example Output

🧩 Example goal state achieved:

1 2 3
4 5 6
7 8 _


🏁 Output:

Solved in 28 moves.

🧑‍💻 Tech Stack

Language: Python 3.x

GUI Library: Tkinter

Algorithm: A* Search

Heuristic: Manhattan Distance

📁 Project Structure
AI/
├── 8_Puzzle_Problem.py   # Main Python file
├── README.md             # Project documentation
└── .gitignore            # (optional)

🏆 Future Enhancements

🚀 Add visual A* search visualization
🧩 Implement 15-Puzzle (4x4 version)
🎨 Add theme customization
💾 Save and load puzzle states

🧑‍🎓 Author

Kiran S
🔗 GitHub: SKiran-Hub

💬 Always open to feedback and collaboration!

📜 License

This project is licensed under the MIT License — feel free to use, modify, and share it with credit.

⭐ If you like this project, please star it on GitHub!
Your support motivates me to build more AI-based projects 😊