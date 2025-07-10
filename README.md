# Tic Tac Toe Game

A colorful command-line implementation of the classic Tic Tac Toe game built in Python, featuring human vs computer gameplay with intelligent AI moves.

## Features

- **Interactive Gameplay**: Player vs Computer with intuitive controls
- **Colorful Interface**: Uses ANSI color codes for enhanced visual experience
  - Blue X for player moves
  - Red O for computer moves
  - Colored prompts and messages
- **Smart Input System**:
  - Row selection using letters (A, B, C)
  - Column selection using numbers (1, 2, 3)
- **Intelligent AI**: Computer makes strategic moves (with room for enhancement)
- **Game Loop**: Option to play multiple rounds
- **Cross-Platform**: Automatic console clearing for Windows and Unix systems

## Game Preview

```
    1   2   3
 A  X | O | -
   ---+---+---
 B  - | X | -
   ---+---+---
 C  - | - | O
```

## Requirements

- Python 3.x
- No external dependencies required

## Installation

1. Clone or download the repository
2. Ensure you have Python 3.x installed
3. Navigate to the project directory

## How to Play

1. Run the game:

   ```bash
   python main.py
   ```

2. **Making Moves**:

   - Choose a row by entering A, B, or C
   - Choose a column by entering 1, 2, or 3
   - Your X will be placed in the selected position

3. **Winning**:

   - Get three X's in a row (horizontally, vertically, or diagonally)
   - The computer will try to win or block your moves

4. **Game End**:
   - The game announces the winner
   - Choose 'y' to play again or 'n' to quit

## File Structure

```
Tic_Tac_Toe/
├── main.py          # Main game loop and user interface
├── tictactoe.py     # TicTacToe class with game logic
├── README.md        # This file
└── __pycache__/     # Python cache files
```

## Code Architecture

### `main.py`

- Handles user input and game flow
- Manages the game loop and replay functionality
- Provides colorful console interface
- Implements input validation

### `tictactoe.py`

- Contains the `TicTacToe` class with core game logic
- Manages the game board state
- Implements win detection algorithms
- Handles computer AI moves

## Game Logic

### Win Detection

The game checks for wins in three ways:

1. **Horizontal**: Three symbols in any row
2. **Vertical**: Three symbols in any column
3. **Diagonal**: Three symbols in either diagonal

### Computer AI

Currently implements random move selection with commented code for smarter AI that can:

- Win in the next move if possible
- Block player wins
- Make strategic moves

## Future Enhancements

The codebase includes TODO comments for potential improvements:

- [ ] Implement smarter AI logic (partially coded in comments)
- [ ] Enhanced win detection
- [ ] Better input validation
- [ ] Score tracking across multiple games

## Development Notes

- Uses ANSI escape codes for colored output
- Implements proper input validation for both row and column selection
- Includes cross-platform console clearing functionality
- Modular design with separate game logic and UI components

## Contributing

Feel free to contribute to this project by:

1. Implementing the smarter AI logic
2. Adding new features
3. Improving the user interface
4. Adding unit tests

## License

This project is open source and available under the MIT License.

---

_Developed as part of Python Professional Projects_
