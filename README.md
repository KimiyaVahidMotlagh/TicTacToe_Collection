#  Tic-Tac-Toe Collection
This repository contains two versions of the classic Tic-Tac-Toe game implemented in Python using the Tkinter library: 
a 4x4 version with an advanced AI and a 3x3 version with a simpler AI. These projects are designed to demonstrate GUI programming, 
game AI development, and event-driven programming using Python.

## Table of Contents
- [GUI Description](https://github.com/KimiyaVahidMotlagh/TicTacToe-Collection#gui-description)
- [AI Opponent](https://github.com/KimiyaVahidMotlagh/TicTacToe-Collection#ai-opponent)
- [How to Play](https://github.com/KimiyaVahidMotlagh/TicTacToe-Collection#how-to-play)
- [Contributing](https://github.com/KimiyaVahidMotlagh/TicTacToe-Collection#contributing)

## GUI Description
In both versions, there are main GUI features which can be implemented using Tkinter in Python:
- Main Window: Configured with a title, fixed minimum size, and centered placement for optimal user experience.
- Game Grid: Implemented with buttons that serve as the interactive cells within the Tic-Tac-Toe grid.
- Status Updates: A dedicated label that dynamically updates to reflect the current game status.
- Themes: Consistent and customizable themes applied across all UI components.
- Hover Effects: Buttons change appearance on hover to indicate interactivity.
- Layout Management: Utilizes Tkinter's packing and grid systems for clean and scalable layout designs.
- Restart Button: Allows players to reset the game at any time, promoting continuous play without disruption.

  
## AI Opponent
While the 3x3 AI provides a good challenge without being overly difficult, the 4x4 AI offers a significantly tougher challenge due to the 
increased complexity and possible combinations.

#### General AI Features
- Immediate Win Recognition: The AI scans the board for potential immediate winning moves before making a decision, 
ensuring that if a win is possible in one move, it will take it.
- Block Opponent Wins: If the AI detects that the player is one move away from winning, it prioritizes blocking that move over other strategies.
- Optimal Move Selection: Utilizes strategic placement and predictive outcomes to make moves that will either
lead to its win or prevent the player from setting up a future win.

#### 3x3 Tic-Tac-Toe AI
- Simple Tactical Play: In the 3x3 version, the AI follows a basic tactical algorithm that focuses on blocking player moves and taking any immediate winning opportunities.
This version is ideal for beginners and casual play.
- Center and Corner Play: Prioritizes capturing the center and corner cells, which are strategically advantageous in Tic-Tac-Toe.
- 
#### 4x4 Tic-Tac-Toe AI
- Advanced Algorithm with Minimax and Alpha-Beta Pruning: This AI uses the minimax algorithm optimized with alpha-beta pruning to reduce the computation of
unnecessary moves, making it more efficient and faster in decision-making.
- Transposition Table: Employs a transposition table to store previously evaluated board states, which dramatically speeds up the AI
by avoiding recalculating the same scenarios.
- Persistent Learning: In the 4x4 version, the AI learns from each game by storing successful moves from initial plays, allowing it to improve its opening strategy over time.


## How to Play
- Start the Game: Open the application to see the game grid.
- Make Your Move: Click on an empty cell to place your "X".
- Play Against AI: The AI will make its move with "O" following your turn.
- Check for Win or Tie: The game declares a winner or a tie based on the board's state.
- Restart Anytime: Use the restart button to clear the board and start a new game immediately.


## Contributing
Contributions to enhance the games or documentation are highly appreciated. Please fork the repository, make your changes, and submit a pull request.
