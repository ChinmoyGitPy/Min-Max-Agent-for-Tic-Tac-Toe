import random

#board

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("\n")
    for i,r in enumerate(board):
        print(' | '.join(r))
        if i < 2:
            print("--+---+--")
    print("\n") 
def moves_left(board):
    return any(" " in r for r in board)

def check_winner(board):
    
    for r in board:
        if r[0] == r[1] == r[2] and r[0] != " ":
            return r[0]
        
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] and board[0][c] != " ":
            return board[0][c]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    
    return None

#minimax algorithm (the hard part)

def minimax(board,depth,is_max):
    winner = check_winner(board)
    if winner == "X":
        return 10 - depth
    elif winner == "O":
        return depth -10
    elif not moves_left(board):
        return 0
    
    if is_max:
        best = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best,minimax(board,depth+1,False))
                    board[i][j] = " "
        return best
    else:
        best = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best,minimax(board,depth+1,True))
                    board[i][j] = " "
        return best
    
def minimax_agent(board):
    best_val = -float("inf")
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(board,0,False)
                board[i][j] = " "

                if move_val > best_val:
                    best_val = move_val
                    best_move = (i,j)

    return best_move

#random agent

def random_agent(board):
    moves = [(i,j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(moves)

#the game

def play_game(agentx,agento,verbose=False):
    board = create_board()
    current = "X"

    while True:
        if verbose:
            print_board(board)
        if current == "X":
            move = agentx(board)
        else:
            move = agento(board)
        if move is None:
            return "Draw"
        
        board[move[0]][move[1]] = current

        winner = check_winner(board)
        if winner:
            if verbose:
                print_board(board)
            return winner
        if not moves_left(board):
            if verbose:
                print_board(board)
            return "Draw"
        
        current = "O" if current == "X" else "X"

def human(board):
        while True:
            try:
                r = int(input("Row (0-2): "))
                c = int(input("Column (0-2): "))
                if board[r][c] == " ":
                    return (r,c)
                else:
                    print("Cell occupied, try again.")
            except:
                print("Invalid input, try again.")

def play_terminal():
    print("You are O, the AI is X")
    result = play_game(minimax_agent,human,verbose=True)
    print("Result:", result)

def simulate_games(n,agentx,agento):
    results = {"X":0,"O":0,"Draw":0}
    for z in range(n):
        result = play_game(agentx,agento,verbose=False)
        results[result] += 1
    
    print("\nSimulation Results:")
    print(f"Total games: {n}")
    print(f"X wins: {results['X']}")
    print(f"O wins: {results['O']}")
    print(f"Draws: {results['Draw']}")
    print(f"Win rate (X): {results['X']/n*100:.2f}%")

if __name__ == "__main__":
    print("1. Play VS AI")
    print("2. Simulate AI vs Random")
    
    choice = input("select: ")

    if choice == "1":
        play_terminal()
    elif choice == "2":
        n = int(input("No. of simulations: "))
        simulate_games(n,minimax_agent,random_agent)
