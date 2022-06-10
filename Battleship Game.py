from distutils.command.build_scripts import first_line_re
from re import A


def printboard(board):
    letters = "0123456789"
    count = 0
    print("   ", end = ' ')
    for x in range(10):
        print(x, end = ' ')
    print()
    for row in board:
        print(letters[count]," ", end=' ')
        for elem in row:
            print(elem, end=' ')
        print()
        count+=1
def destroyer(board, orientation):
    col = colf()
    row = rowf()
    #valid = isvalid(board,row,col,2,orientation)
    valid = check(board,row,col,2, orientation)
    if valid:
        if orientation == "1":
            for x in range(2):
                while True:
                    if (x == 0 and row < 9) or x == 1:
                        board[row][col] = 'O'
                        row+=1
                        break
                    else:
                        print("Destroyer out of Bounds. Choose Row Again")
                        row = int(input("Choose Starting Row (0-8): "))
                        if check(board,row,col,2, orientation):
                            pass
                        else:
                            print("Ships must not be beside each other! choose again")
                            destroyer(board,orientation)  
                            break 
        else:
            for y in range(2):
                while True:
                    if (y == 0 and col < 9) or y == 1:
                        board[row][col] = 'O'
                        col+=1
                        break
                    else:
                        print("Destroyer out of Bounds. Choose Column Again")
                        col = int(input("Choose Starting Column (0-8): "))
                        if check(board,row,col,2, orientation):
                            pass
                        else:
                            print("Ships must not be beside each other! choose again")
                            destroyer(board,orientation)  
                            break 
    else:
        print("Ships must not be beside each other! choose again")
        destroyer(board,orientation)   
def submarine(board, orientation):
    col = colf()
    row = rowf()
    #valid = isvalid(board,row,col,3,orientation)
    valid = check(board,row,col,3, orientation)
    if valid:
        if orientation == "1":
            for x in range(3):
                while True:
                    if (x == 0 and row < 8) or (x == 1 and row < 9) or x == 2:
                        board[row][col] = 'O'
                        row+=1
                        break
                    else:
                        print("Submarine out of Bounds. Choose Row Again")
                        row = int(input("Choose Starting Row (0-7): "))
                        if check(board,row,col,3, orientation):
                            pass
                        else:
                            print("Ships must not be beside each other! choose again")
                            submarine(board, orientation)
                            break 
        else:
            for y in range(3):
                while True:
                    if (y == 0 and col < 8) or (y == 1 and col < 9) or y == 2:
                        board[row][col] = 'O'
                        col+=1
                        break
                    else:
                        print("Submarine out of Bounds. Choose Column Again")
                        col = int(input("Choose Starting Column (0-7): "))
                        if check(board,row,col,3, orientation):
                            pass
                        else:
                            print("Ships must not be beside each other! choose again")
                            submarine(board, orientation)
                            break 
    else:
        print("Ships must not be beside each other! choose again")
        submarine(board,orientation)
def cruiser(board, orientation):
    col = colf()
    row = rowf()
    #valid = isvalid(board,row,col,3,orientation)
    valid = check(board,row,col,3, orientation)
    if valid:
        if orientation == "1":
            for x in range(3):
                while True:
                    if (x == 0 and row < 8) or (x == 1 and row < 9) or x == 2:
                        board[row][col] = 'O'
                        row+=1
                        break
                    else:
                        print("Cruiser out of Bounds. Choose Row Again")
                        row = int(input("Choose Starting Row (0-7): "))
                        if check(board,row,col,3, orientation):
                            pass
                        else:
                            print("Ships must not be beside each other! choose again")
                            cruiser(board, orientation)
                            break 
        else:
            for y in range(3):
                while True:
                    if (y == 0 and col < 8) or (y == 1 and col < 9) or y == 2:
                        board[row][col] = 'O'
                        col+=1
                        break
                    else:
                        print("Cruiser out of Bounds. Choose Column Again")
                        col = int(input("Choose Starting Column (0-7): "))
                        if check(board,row,col,3, orientation):
                            pass
                        else:
                            print("Ships must not be beside each other! choose again")
                            cruiser(board, orientation)
                            break 
    else:
        print("Ships must not be beside each other! choose again")
        cruiser(board,orientation)  
def battleship(board, orientation):
    col = colf()
    row = rowf()
    #valid = isvalid(board,row,col,4,orientation)
    valid = check(board,row,col,4, orientation)
    if valid:
        if orientation == "1":
            for x in range(4):
                while True:
                    if (x == 0 and row < 7) or (x == 1 and row < 8) or (x == 2 and row < 9) or x == 3:
                        board[row][col] = 'O'
                        row+=1
                        break
                    else:
                        print("Battleship out of Bounds. Choose Row Again")
                        row = int(input("Choose Starting Row (0-6): "))
                        if check(board,row,col,4, orientation):
                            pass
                        else:
                            print("Ships must not be beside each other! choose again")
                            battleship(board, orientation)
                            break 
        else:
            for y in range(4):
                while True:
                    if (y == 0 and col < 7) or (y == 1 and col < 8) or (y == 2 and col < 9) or y == 3:
                        board[row][col] = 'O'
                        col+=1
                        break
                    else:
                        print("Battleship out of Bounds. Choose Column Again")
                        col = int(input("Choose Starting Column (0-6): "))
                        if check(board,row,col,4, orientation):
                            pass
                        else:
                            print("Ships must not be beside each other! choose again")
                            battleship(board, orientation)
                            break 
    else:
        print("Ships must not be beside each other! choose again")
        battleship(board,orientation)
def aircraft(board, orientation):
    col = colf()
    row = rowf()
    #valid = isvalid(board,row,col,5,orientation)
    valid = check(board,row,col,5, orientation)
    if valid:
        if orientation == "1":
            for x in range(5):
                while True:
                    if (x == 0 and row < 6) or (x == 1 and row < 7) or (x == 2 and row < 8) or (x == 3 and row < 9) or x == 4:
                        board[row][col] = 'O'
                        row+=1
                        break
                    else:
                        print("Aircraft out of Bounds. Choose Row Again")
                        row = int(input("Choose Starting Row (0-5): "))
                        if check(board,row,col,5, orientation):
                            pass
                        else:
                            print("Ships must not be beside each other! choose again")
                            aircraft(board, orientation)
                            break 
        else:
            for y in range(5):
                while True:
                    if (y == 0 and col < 6) or (y == 1 and col < 7) or (y == 2 and col < 8) or (y == 3 and col < 9) or y == 4:
                        board[row][col] = 'O'
                        col+=1
                        break
                    else:
                        print("Aircraft out of Bounds. Choose Column Again")
                        col = int(input("Choose Starting Column (0-5): "))
                        if check(board,row,col,5, orientation):
                            pass
                        else:
                            print("Ships must not be beside each other! choose again")
                            aircraft(board, orientation)
                            break 
    else:
        print("Ships must not be beside each other! choose again")
        aircraft(board,orientation)
def colf():
    col = 0
    while True:
        try:
            col = int(input("Choose Starting Column (0-9): "))
        except:
            col = 20
        if (col >= 0 and col < 10):
            break
        else:
            print("INPUT INVALID")
    return col
def rowf():
    row = 0
    while True:
        try:
            row = int(input("Choose Starting Row (0-9): "))
        except:
            row = 20
        if (row >= 0 and row < 10):
            break
        else:
            print("INPUT INVALID")
    return row
def add_ships(board):
    for n in range(5):
        print("Only choose either 1 or 2")
        if n == 0:
            print("Inserting Destroyer (2 Squares)")
            print("[1] Vertical \n[2] Horizontal:")
            orientation = orient()
            destroyer (board, orientation)
        elif n == 1:
            print("Inserting Submarine (3 Squares)")
            print("[1] Vertical \n[2] Horizontal:")
            orientation = orient()
            submarine(board, orientation)
        elif n == 2:
            print("Inserting Cruiser (3 Squares)")
            print("[1] Vertical \n[2] Horizontal:")
            orientation = orient()
            cruiser(board, orientation)
        elif n == 3:
            print("Inserting Battleship (4 Squares)")
            print("[1] Vertical \n[2] Horizontal:")
            orientation = orient()
            battleship(board, orientation)
        elif n == 4:
            print("Inserting aircraft (5 Squares)")
            print("[1] Vertical \n[2] Horizontal:")
            orientation = orient()
            aircraft(board, orientation)
        printboard(board1)
def check(board, row, col,type, orientation):
    a= True
    b= True
    c= True
    d= True
    e= True
    f= True
    g= True
    h= True
    i= True
    first = True
    second = True
    third = True
    fourth = True
    fifth = True
    for x in range(type):
        try:
            a = board[row][col] != 'O'
        except: pass
        try:
            b = board[row-1][col-1] != 'O'
        except: pass
        try:
            c = board[row+1][col+1] != 'O'
        except: pass
        try:
            d = board[row+1][col] != 'O'
        except: pass
        try:
            e = board[row-1][col] != 'O'
        except: pass
        try:
            f = board[row][col-1] != 'O'
        except: pass
        try:
            g = board[row][col+1] != 'O'
        except: pass
        try:
            h = board[row-1][col+1] != 'O'
        except: pass
        try:
            i = board[row+1][col-1] != 'O'
        except: pass
        if x == 0:
            first = a and b and c and d and e and f and g and h and i
        elif x == 1:
            second = a and b and c and d and e and f and g and h and i
        elif x == 2:
            third = a and b and c and d and e and f and g and h and i
        elif x == 3:
            fourth = a and b and c and d and e and f and g and h and i
        elif x == 4:
            fifth = a and b and c and d and e and f and g and h and i
        if orientation == "1":
            row += 1
        else:
            col+=1
    return first and second and third and fourth and fifth
def attack(board, qboard):
    while True:
        printboard(qboard)
        print("Attack Enemy")
        shot_col = colf()
        shot_row = rowf()
        
        if qboard[shot_row][shot_col] == '#' or qboard[shot_row][shot_col] == 'X':
            print("You Already hit this box. Please Choose Again")
        elif board[shot_row][shot_col] == 'O':
            qboard[shot_row][shot_col] = 'X'
            board[shot_row][shot_col] = 'X'
            print("Hit")
            check_sink(board)
            if game_over(board2):
                break
            print("You get another turn.")
        elif board[shot_row][shot_col] == '.':
            qboard[shot_row][shot_col] = '#'
            board[shot_row][shot_col] = '#'
            print("Miss")
            break
        else:
            pass
def check_sink(board):
    a = 0
    if board[0][0] == 'X' and board[1][0] == 'X':
        a += 1
    if board[2][3] == 'X' and board[2][4] == 'X' and board[2][5] == 'X':
        a += 1
    if board[4][2] == 'X' and board[5][2] == 'X' and board[6][2] == 'X':
        a += 1
    if board[9][3] == 'X' and board[9][4] == 'X' and board[9][5]  == 'X' and board[9][6] == 'X':
        a += 1
    if board[0][9] == 'X' and board[1][9]  == 'X' and board[2][9] == 'X' and board[3][9]  == 'X' and board[4][9] == 'X':
        a += 1
    print("Enemy has " + str(a) + " sunken ship/s.")
def game_over(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'O':
                return False
            else:
                pass
    return True
def bot_attack(board, turn):
    print("Enemy Bot Attack")
    n = 0
    turn1 = turn
    if turn1 < 10:
        n = 0
    elif turn1 >= 10 and turn1 <20:
        n = 1
        turn = turn - 20
    elif turn1 >= 20 and turn1 <30:
        n = 2
        turn = turn - 30
    elif turn1 >= 30 and turn1 <40:
        n = 3
        turn = turn - 40
    elif turn1 >= 40 and turn1 <50:
        n = 4
        turn = turn - 50
    elif turn1 >= 50 and turn1 <60:
        n = 5
        turn = turn - 60
    elif turn1 >= 60 and turn1 <70:
        n = 6
        turn = turn - 70
    elif turn1 >= 70 and turn1 <80:
        n = 7
        turn = turn - 80
    elif turn1 >= 80 and turn1 <90:
        n = 8
        turn = turn - 90
    elif turn1 >= 90 and turn1 <100:
        n = 9
        turn = turn - 100
    else:
        pass
    if board[turn][n] == 'O':
        board[turn][n] = 'X'
        print("Enemy Hit")
        return True
    elif board[turn][n] == '.':
        board[turn][n] = '#'
        print("Enemy Missed")
        return False
    else:
        print("Mali")
def bot_won(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'O':
                return False
            else:
                pass
    return True
def orient():
    while True:
        x = input("Choose Orientation: ")
        if x == "1" or x == "2":
            break
        else:
            print("INPUT INVALID")
    return x
            
        
  
board1 = [
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.']
         ]
board2 = [
         ['O','.','.','.','.','.','.','.','.','O'],
         ['O','.','.','.','.','.','.','.','.','O'],
         ['.','.','.','O','O','O','.','.','.','O'],
         ['.','.','.','.','.','.','.','.','.','O'],
         ['.','.','O','.','.','.','.','.','.','O'],
         ['.','.','O','.','.','.','.','.','.','.'],
         ['.','.','O','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','.','.','.','.','.','.','.'],
         ['.','.','.','O','O','O','O','.','.','.']
         ]
board3 = [
         ['?','?','?','?','?','?','?','?','?','?'],
         ['?','?','?','?','?','?','?','?','?','?'],
         ['?','?','?','?','?','?','?','?','?','?'],
         ['?','?','?','?','?','?','?','?','?','?'],
         ['?','?','?','?','?','?','?','?','?','?'],
         ['?','?','?','?','?','?','?','?','?','?'],
         ['?','?','?','?','?','?','?','?','?','?'],
         ['?','?','?','?','?','?','?','?','?','?'],
         ['?','?','?','?','?','?','?','?','?','?'],
         ['?','?','?','?','?','?','?','?','?','?']
         ]

printboard(board1)
print("\n")
add_ships(board1)
print("\n")
turn = 0
while True:
    attack(board2, board3)
    if game_over(board2):
        print("Game Over You Won.")
        break
    
    while True:
        if bot_attack(board1, turn):
            turn+=1
        else:
            turn+=1
            break
    printboard(board1)
    print("this is the value of turn " + str(turn))
    if bot_won(board1):
        print("Game Over You Lost. Drink Milk")
        break
    
    


