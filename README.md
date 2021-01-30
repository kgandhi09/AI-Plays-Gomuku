# AI-Gomoku

## AI agent for playing Gomoku
This project is part of class CS4341: Intro to AI. The chalenge was to design an artificialy intelligent game plaing agent for Gomuku. Gomoku is a tic-tac like game in which player has to achieve 5 in a row on a 15 by 15 board to win the game. The part of the challenge required the agent to come up with the best possible move within 9 seconds. The team implemented Minimax algorithm and alpha beta pruning to find the best move possible.  

### Utility Function
Our evaluation or utility function generates or assigns a score to a particular board state. This evaluation function is a sub part used by our minimax function. When the Minimax function generates and tries different positions for each player, the evaluation function estimates the goodness of that boardstate based on which the minimax choses the best possible move. Our evaluation function takes into account; both offensive score and defensive score which represents the relative difference of winning or losing.

Firstly, the function takes into consideration how many consecutive squares the team occupies and how many sets of these series are present in the board. Then we calculate the number of open ends available for the player to move before or/and after these consecutive series which represents the chances of achieving five in a row. This procedure is followed across three dimensions: row, column and diagonal.

### Heuristics and/or strategies that we employed to decide how to expand the minimax tree without exceeding the given time limit and avoid expanding the entire game tree:
- Using the “depth” attribute in the Minimax implementation: The “depth” attribute is usually compared with a set “max depth” as limit to avoid expanding the whole tree.
- Moving nearby our AI’s / Opponent’s last move: At every point of minimax, considering only moves related to our AI’s last move or our opponent’s last move. We implement this by using a set fixed sized grid (a portion on the board) and playing valid moves in that grid. We have set the size of this grid as 5X5

#### For more details and performance of our AI agent, please have a look at: https://drive.google.com/file/d/15Xn7RVABVLyX6nxz4WL9GL3EIWdHe-XX/view?usp=sharing 
