This is a simple tic tac toe game and I have used the mini-max algorithm to make the game's AI.

Below explains how I integrated the algorithm and how it works, if you're not interested you can scroll to the bottom to see how to play the game!

First I laid out of the logic behind how my agent will work. 
Since I have decided to use the mini-max algorithm to make my tic tac toe agent it's crucial to understand it's logic to program it.

The rules of tic tac toe are simple.

1. Two players play the game and one starts first.
2. The players place the "X" or "O" sign in any of the empty spaces of a 3*3 grid.
3. The first player to get 3 consecutive signs either vertically, diagonally or horizontally wins the match.

We can prove mathematically that the game itself is proven and has 100% draw rate if both players play the most optimal moves.

So how does a mini-max algorithm work? And why are we using this algorithm to make our agent?

The mini-max algorithm is a decision making algorithm, it anticipates possible future positions and tries to get the most optimal moves.

The key components of the mini-max algorithm is the evaluation function and the minimising and maximising player.

The evaluation function assigns a score for a certain board state. This helps the algorithm to filter out nodes from the game tree.
The game tree is a tree of nodes that are the possible states of a game. Each state results in different outcome based on the input.
The depth of a tic tac toe game tree is comparatively shallow which is only 9. So there should be 9! possible positions but we have to look for the invalid positions too,
so the actual possible positions in a tic tac toe game is 5,478. This is computationally small, so minimal hardware requirement is needed for a tic tac toe agent.
While the game trees of games like connect 4 are much deeper, it's not computationally possible to create the perfect mini-max agent for it.
Therefore we can conclude that the tic tac toe mini-max algorithm is certainly going to win or draw a match.

We assign +1 (a winning case)
          0 (a draw)
         -1 (a loosing case)

        for every board base cases i.e, terminal states possible

Now as it is given in the image, these values are set to the certain base cases of the game tree.

For using this evaluation system we assign one of the player the minimising player and one of the player the maximising player.
The maximising player that is our agent has to find the situation where it has the best chance of winning, whereas the minimising player that is our opponent is forced to take equal or worse options.

The algorithm functions in a 3 phase system.

1. Base Case 
2. Recursive Exploration
3. Back Tracking 

First as we have noted that the algorithm sets values for all 3 base cases, then it starts exploring all possible endings recursively,
after collecting all endings it back tracks to the one that has the maximum profit for the agent considering the opponent picks the best ones. 

Then the algorithm keeps looping this 3 phase system to the end.


How to play ----->

 Run the script and you will see two options in the interface,
 
 1.Play VS AI
 2.Simulate AI vs Random

 Select 1 if you want to play with it, the AI starts first and it is X, you are O.
 Select 2 if you want to simulate games of the AI against another AI that picks random moves. (the minimax AI doesn't loose anyways :D)

