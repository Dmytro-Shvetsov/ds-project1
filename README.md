# Tic-Tac-Toe game

---
### How to run it?

1. clone the repo to your PC
2. install gRPC
3. Open 3 terminals
4. For each terminal run "python ./node.py {i}". Where "i: is a node id from 0 to 2.
5. Play a game!

### List of commands

Start_game:
  * Starts the game, chooses the leader and syncs the clock.
  
Set_symbol:
  * Set symbol (pos, type). Where pos is position on the board from 0 to 8 and type is "X" or "O"
  
List_board:
  * Returns the current state of the board to the player.
  
Set_node_time:
  * Sets the time for the current node
  
 Set_time_out:
  * Sets the timeout for the players 
