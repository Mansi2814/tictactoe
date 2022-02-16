def showPositions():
    for i in range(3):
        print(f"\t {3*i+1} | {3*i+2} | {3*i+3}") 
        if i<2:
            print("\t ---------")

def emptyPositions(board):
    print("You can choose following positions: ", end=" ")
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                print(3*i+j+1, end=" ")
    print()

def initializeBoard(board = []):
    for i in range(3):
        board.append([' ']*3)
    return board

def showBoard(board):
    for i in range(3):
        print(f"\t {board[i][0]} | {board[i][1]} | {board[i][2]}") 
        if i<2:
            print("\t ---------") 
    print()

def diagnolMatch(board):
    i=0
    if board[i][i]==board[i+1][i+1]==board[i+2][i+2] and board[i][i]!=' ':
        return True
    if board[0][2]==board[1][1]==board[2][0] and board[0][2]!=' ':
        return True
    return False

def columnMatch(board):
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i] and board[0][i]!=' ':
            return True
    return False

def rowMatch(board):
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] and board[i][0]!=' ':
            return True
    return False

def gameOver(board):
    if rowMatch(board) or columnMatch(board) or diagnolMatch(board):
        return True
    return False

def minimax(board, moves, whoseTurn):
    if gameOver(board):
        if whoseTurn==HUMAN:
            return 10
        else:
            return -10
    if moves==9:
        return 0
    if whoseTurn==COMPUTER:
        bestScore=-999
        for i in range(3):
            for j in range(3):
                if board[i][j]==' ':
                    board[i][j]=COMPUTER
                    score= minimax(board, moves+1, HUMAN)
                    board[i][j]=' '
                    if score>bestScore:
                        bestScore=score
        return bestScore
    else:
        bestScore=999
        for i in range(3):
            for j in range(3):
                if board[i][j]==' ':
                    board[i][j]=HUMAN
                    score = minimax(board, moves+1, COMPUTER)
                    board[i][j]=' '
                    if score<bestScore:
                        bestScore = score
        return bestScore


def bestMove(board, moves, whoseTurn):
    bestScore=-999
    if whoseTurn==COMPUTER:
        for i in range(3):
            for j in range(3):
                if board[i][j]==' ':
                    board[i][j]=COMPUTER
                    score = minimax(board, moves+1, HUMAN)
                    board[i][j]=' '
                    if score>bestScore:
                        bestScore = score
                        x=i
                        y=j
        board[x][y]=COMPUTER

def startGame(whoseTurn, board):
    moves = 0
    while(moves<9 and not gameOver(board)):
        if whoseTurn==HUMAN:
            emptyPositions(board)
            print("Choose a position: ")
            h = int(input(" "))
            x = (h-1)//3
            y = (h-1)%3
            if board[x][y]==' ':
                board[x][y]=HUMAN
                moves+=1
                whoseTurn=COMPUTER
                showBoard(board)
            else:
                print("Invalid Choice")
        else:
            bestMove(board, moves, COMPUTER)
            moves+=1
            whoseTurn=HUMAN
            showBoard(board) 

    if gameOver(board):
        if whoseTurn==HUMAN:
            print("Computer Won")
        else:
            print("Player Won")
    else:
        print("It's a draw")

if __name__=='__main__':
    HUMAN = "O"
    COMPUTER = "X"
    board = initializeBoard()
    showPositions()
    print("Do you want to be the first player?(y/n)", end = " ")
    n = input()
    if n == 'y':
        startGame(HUMAN, board)
    elif n == 'n':
        startGame(COMPUTER, board)
    else:
        print("Invalid Choice")
