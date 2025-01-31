
# Who Has More Followers? - Python Turtle Game

A fun and interactive game where you guess which celebrity or public figure has more social media followers. Built using Python's Turtle graphics library.

![image](https://github.com/user-attachments/assets/fe635c9e-05cb-40b8-8389-fe45b041a44a)

## Description

Test your knowledge of social media popularity! Two random accounts are displayed (A and B), and you must guess which one has a higher follower count. The game keeps track of your score, but one wrong guess ends the game!

## Prerequisites

- Python 3.x
- `turtle` module (comes with standard Python library)


## How to Play

1. **Run the game**:
   ```bash
   python main.py
   ```
2. **Controls**:
   - Press `A` to choose Account A
   - Press `B` to choose Account B
3. **Gameplay**:
   - Correct guesses increase your score.
   - Incorrect guesses end the game immediately.

## Features

- 🎯 **Compare Accounts**: Randomly selects two accounts to compare.
- 📊 **Score Tracking**: Real-time score updates.
- ✅ **Immediate Feedback**: Visual indicators for correct/wrong answers.
- 🎨 **Colorful UI**: Clean interface with colored text and emojis.

## Code Structure

Key functions:
- `draw_text()`: Renders text on the screen.
- `format_data()`: Formats account data for display.
- `draw_screen()`: Updates the game interface.
- `check_answer()`: Validates user input and updates game state.

## Customization

1. **Data**: Modify `game_data.py` to add/remove accounts.
2. **Styling**: Adjust colors, fonts, and positions in `draw_text()` and `draw_screen()`.
3. **Game Rules**: Change scoring logic or add lives in `check_answer()`.

## Possible Enhancements

- Add more account data in `game_data.py`.
- Include profile images (requires additional Turtle setup).
- Implement a high-score system.
- Add sound effects for correct/incorrect answers.

## Troubleshooting

- **Missing `game_data.py`**: Ensure both files are in the same directory.
- **Duplicate Accounts**: Code automatically handles duplicates, but ensure `game_data.py` has enough entries.

#

**Challenge yourself and see how high you can score!** 
