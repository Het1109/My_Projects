

# Blackjack Game in Python

![Python](https://img.shields.io/badge/Python-3.x-blue)  
![Blackjack](https://img.shields.io/badge/Game-Blackjack-green)  
![ASCII Art](https://img.shields.io/badge/Art-ASCII-orange)

This project is a **Blackjack Game** implemented in Python. It allows users to play a simplified version of the classic casino game against the computer. The game includes features like card dealing, score calculation, and a comparison of scores to determine the winner.

---

## Features

- **Card Dealing**: Randomly deals cards to the player and the computer.
- **Score Calculation**: Automatically calculates the score for both the player and the computer.
- **Blackjack Detection**: Detects if either the player or the computer has a Blackjack (21 with two cards).
- **Ace Handling**: Adjusts the value of Ace (11 or 1) based on the score.
- **Interactive Gameplay**: Allows the player to hit (draw another card) or stand (end their turn).
- **ASCII Art**: Displays a stylish logo at the start of the game.

---

## How It Works

Blackjack is a card game where the goal is to have a hand value as close to 21 as possible without exceeding it. The game follows these rules:
1. The player and the computer are dealt two cards each.
2. The player can choose to "hit" (draw another card) or "stand" (end their turn).
3. The computer must draw cards until its score is at least 17.
4. The scores are compared, and the winner is determined.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/blackjack-python.git
   cd main-python
   ```

2. **Run the Program**:
   Ensure you have Python 3.x installed. Run the following command:
   ```bash
   python main.py
   ```

---

## Usage

1. Start the game by typing `y` when prompted.
2. You will be dealt two cards, and the computer will show one card.
3. Type `y` to hit (draw another card) or `n` to stand (end your turn).
4. The computer will automatically draw cards until its score is at least 17.
5. The final scores are compared, and the winner is announced.

---

## Screenshots

![Screenshot from 2025-01-29 19-21-33](https://github.com/user-attachments/assets/d6bfefad-c294-4a9f-969e-c8f0aa090230)
![image](https://github.com/user-attachments/assets/c3d324b1-ff0d-45c5-9dd7-a0af391948ac)



---

## Code Structure

- **`main.py`**: Contains the main logic for the Blackjack game, including card dealing, score calculation, and game flow.
- **`art.py`**: Contains the ASCII art logo displayed at the start of the game.

---

## Dependencies

- Python 3.x
- `random` module (included in Python's standard library)

---

## Contributing

Contributions are welcome! If you'd like to improve this project, feel free to open an issue or submit a pull request.

---


## Acknowledgments

- Inspired by the classic Blackjack game.
- Built with Python for a fun and interactive experience.

---

Enjoy playing Blackjack with this fun and educational project! 🚀

