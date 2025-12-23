'''
Name: Wesley Steem, ID: 1898878
Project-2 deadline: December 20th

In this homework, you will creaet a Gomoku game (also called Five in a Row). Gomoku is a board game played
on a grid, so we'll use a Cartesian coordinate system with X-Y coordinates. It is a two-player game
(in your program, one player will be the computer and the other will be you).

Our Gomoku will use an m x n board (note that m and n can be different). The human player will use the stone
'O', and the computer will use 'X'.
'''
#Gomuku Game
#set global variables to store last human move
input_row = 0 
input_col = 0

#Print board
def Print_Board():
    'function Print_Board() takes no parameters and prints a board based on global variables m and n'
    #Prints Top Row of Numbers of the board
    string1 = '   '
    string2 = ''
    for i in range(1, n+1):
        i = str(i)
        string2 += i + ' '
    stringTop = string1 + string2
    print(stringTop)

    #Prints the top row of +-+-+-+-+
    plusMinus = '  +'
    end = '-+'*n
    plusMinusEnd = plusMinus + end
    print(plusMinusEnd)

    #Outer loop to print +-+-+- between each row and start each row
    for j in range(1, m+1):
        g = str(j)
        begString = '{0:2}|'.format(g)
        #Inner for loop to print '|' between each empty space in board
        blankSpots = ''
        for i in range(1, n+1):
            blankSpots += (board[j-1][i-1] + '|')
        #concatenate everything together
        firstRow = begString + blankSpots + '\n' + plusMinusEnd
        #print it all!
        print(firstRow)

#Human Turn
def Human_Turn():
    'function Human_Turn() takes no parameters and places human stone based on user input'
    print('=============\nHuman\'s Turn\n=============')
    while True: #use try and except to make sure user inputs valid x and y values
        try: 
            x = input('Input the ROW where you want to put your stone between 1 and {}: '.format(m))
            x = int(x)
            if x in range(1, m+1):
                break
            elif x not in range(1, m+1):
                print('Wrong Input.')
        except:
            print('Wrong Input.')
    while True:
        try:
            y = input('Input the COLUMN where you want to put your stone between 1 and {}: '.format(n))
            y = int(y)
            if y in range(1, n+1):
                break
            elif y not in range(1, n+1):
                print('Wrong Input.')
        except:
            print('Wrong Input.')
    #Check if the spot is already taken
    while board[x-1][y-1] != ' ':
        print('The spot ({}, {}) has already been take!!'.format(x, y))
        while True: #use try and except to make sure user inputs valid x and y values if spot is taken
            try: 
                x = input('Input the ROW where you want to put your stone between 1 and {}: '.format(m))
                x = int(x)
                if x in range(1, m+1):
                    break
            except:
                print('Wrong Input.')
        while True:
            try:
                y = input('Input the COLUMN where you want to put your stone between 1 and {}: '.format(n))
                y = int(y)
                if y in range(1, n+1):
                    break
            except:
                print('Wrong Input.')
    board[x-1][y-1] = 'O'
    print('================\nHuman\'s Choice is {}, {}\n================'.format(x, y))
    Print_Board()
    global input_row, input_col
    input_row = x - 1
    input_col = y - 1

    #Check for a win after humans turn
    return Check_Connected_num(input_row, input_col, 'O')

#Random Machine Turn
def Random_Machine_Turn():
    'function Random_Machine_Turn() takes no parameters and places machines stone randomly'
    print('=====================\nRandom Machine\'s Turn\n=====================')
    import random
    x = random.randrange(1, m+1)
    y = random.randrange(1, n+1)
    while board[x-1][y-1] != ' ':
        x = random.randrange(1, m+1)
        y = random.randrange(1, n+1)
        
    board[x-1][y-1] = 'X'
    print('========================\nRandom Machine\'s Choice is {}, {}\n========================'.format(x, y))
    Print_Board()
    #Check for a win after machine's turn
    winner =  Check_Connected_num(x-1, y-1, 'X')
    return winner

#Check all spots
def All_Spots_Chosen():
    'function All_Spots_Chosen() takes no parameters and checks if all the spots have been filled'
    for j in range(m):
        for i in range(n):
            if board[j][i] == ' ':
                return False
    return True 

#Check rows, columns, and diagonals
def Check_Connected_num(chosen_row, chosen_col, chosen_stone):
    'function Check_Connected_num() takes 3 parameters and checks if there are 5 connected stones in any direction'
    Connected_num = Row_check(chosen_row, chosen_col, chosen_stone)
    if Connected_num >= 5:
        return True
    Connected_num = Column_check(chosen_row, chosen_col, chosen_stone)
    if Connected_num >= 5:
        return True
    Connected_num = Right_Diagonal_check(chosen_row, chosen_col, chosen_stone)
    if Connected_num >= 5:
        return True
    Connected_num = Left_Diagonal_check(chosen_row, chosen_col, chosen_stone)
    if Connected_num >= 5:
        return True
    return False

#row check
def Row_check(input_row, input_col, stone):
    'function Row_check() takes 3 parameters and checks how many stones are connected in the row direction'
    n_after = 0
    col = input_col + 1 #check to the right of the placed stone
    #Check right
    #n is 1 index based, col and row are 0 index based
    while col < n and board[input_row][col] == stone:
        n_after += 1
        col += 1
    n_before = 0
    col = input_col - 1 #check to the left of the placed stone
    while col >= 0 and board[input_row][col] == stone:
        n_before += 1
        col -= 1
    return n_after + n_before + 1

#column check
def Column_check(input_row, input_col, stone):
    'function Column_check() takes 3 parameters and checks connected stones in a column, returning (count, row, col)'
    n_after = 0
    row = input_row + 1 #check below the placed stone
    #Check down
    while row < m and board[row][input_col] == stone:
        n_after += 1
        row += 1
    n_before = 0
    row = input_row - 1 #check above the placed stone
    while row >= 0 and board[row][input_col] == stone:
        n_before += 1
        row -= 1
    return n_after + n_before + 1

#right diagonal check
def Right_Diagonal_check(input_row, input_col, stone):
    'function Right_Diagonal_check() takes 3 parameters and checks how many stones are connected in the right diagonal direction'
    n_after = 0
    row = input_row + 1
    col = input_col + 1 #check down and right of the placed stone
    #Check down and right
    while row < m and col < n and board[row][col] == stone:
        n_after += 1
        row += 1
        col += 1
    n_before = 0
    row = input_row - 1
    col = input_col - 1 #check up and left of the placed stone
    while row >= 0 and col >= 0 and board[row][col] == stone:
        n_before += 1
        row -= 1
        col -= 1
    return n_after + n_before + 1

#left diagonal check
def Left_Diagonal_check(input_row, input_col, stone):
    'function Left_Diagonal_check() takes 3 parameters and checks how many stones are connected in the left diagonal direction'
    n_after = 0
    row = input_row + 1
    col = input_col - 1 #check down and left of the placed stone
    #Check down and left
    while row < m and col >= 0 and board[row][col] == stone:
        n_after += 1
        row += 1
        col -= 1
    n_before = 0
    row = input_row - 1
    col = input_col + 1 #check up and right of the placed stone
    while row >= 0 and col < n and board[row][col] == stone:
        n_before += 1
        row -= 1
        col += 1
    return n_after + n_before + 1

def Place_And_Check_Move(row, col):
    'Places stone X at (row, col), prints choice, prints board, checks for win, and returns winner status'
    board[row][col] = 'X'
    print('===============\nSmart Machine\'s Choice is {},{}\n==============='.format(row+1, col+1))
    Print_Board()
    return Check_Connected_num(row, col, 'X')
'''
def Check_Both_Sides_Empty():
    'function Check_Both_Sides_Empty() checks if the longest chain of O\'s has empty spaces on both ends'
    global input_row, input_col
    max_pos = max(Row_check(input_row, input_col, 'O'), 
                  Column_check(input_row, input_col, 'O'), 
                  Right_Diagonal_check(input_row, input_col, 'O'), 
                  Left_Diagonal_check(input_row, input_col, 'O')) 
    # --- Row Check ---  
    if max_pos == Row_check(input_row, input_col, 'O'):
        # Check right
        row = input_row
        col = input_col
        # Use n for boundary check 
        while col < n and board[row][col] == 'O': 
            col += 1
        # If the next spot is within bounds and empty, place X
        if col < n and board[row][col] == ' ':
            return Place_And_Check_Move(row, col)
            
        # Check left
        row = input_row # Reset row to input_row for left check
        col = input_col # Reset col to input_col for left check
        while col >= 0 and board[row][col] == 'O':
            col -= 1
        # If the calculated spot is within bounds (col >= 0) and empty, place X
        if col >= 0 and board[row][col] == ' ':
            return Place_And_Check_Move(row, col)
'''

#Smart Machine Turn
def Smart_Machine_Turn():
    'function Smart_Machine_Turn() takes no parameters and places stone X based on human\'s last move'
    global input_row, input_col
        
    print('=====================\nSmart Machine\'s Turn\n=====================')
    max_pos = max(Row_check(input_row, input_col, 'O'), 
                  Column_check(input_row, input_col, 'O'), 
                  Right_Diagonal_check(input_row, input_col, 'O'), 
                  Left_Diagonal_check(input_row, input_col, 'O'))

    # Check if the human has a winning move (Block immediately)... this will fill any empty spots that would create a win for O
    if max_pos < 5: 
        for row in range(m):
            for col in range(n):
                if board[row][col] == ' ': #Check every spot that is empty
                    #Temperarily check if placing an O here would create a winning move
                    board[row][col] = 'O'
                    if (Row_check(row, col, 'O') >= 5 or 
                        Column_check(row, col, 'O') >= 5 or 
                        Right_Diagonal_check(row, col, 'O') >= 5 or 
                        Left_Diagonal_check(row, col, 'O') >= 5):
                        
                        # If it does, place an X there instead of the temperary 'O'
                        # Use the new helper function to place, print, and check
                        board[row][col] = 'X' # Place the X for the helper to print/check
                        return Place_And_Check_Move(row, col)
                    else:
                        board[row][col] = ' ' #If it does not create a winning move, reset the spot to empty
                        
    
    # --- Row Blocking Logic ---
    if max_pos == Row_check(input_row, input_col, 'O'):
        # Check right
        row = input_row
        col = input_col
        # Use n for boundary check 
        while col < n and board[row][col] == 'O': 
            col += 1
        # If the next spot is within bounds and empty, place X
        if col < n and board[row][col] == ' ':
            return Place_And_Check_Move(row, col)
            
        # Check left
        row = input_row # Reset row to input_row for left check
        col = input_col # Reset col to input_col for left check
        while col >= 0 and board[row][col] == 'O':
            col -= 1
        # If the calculated spot is within bounds (col >= 0) and empty, place X
        if col >= 0 and board[row][col] == ' ':
            return Place_And_Check_Move(row, col)

    # --- Column Blocking Logic ---
    elif max_pos == Column_check(input_row, input_col, 'O'):
        # Check down
        row = input_row
        col = input_col
        # Use 'm' for boundary check 
        while row < m and board[row][input_col] == 'O':
            row += 1
        # If the next spot is within bounds and empty, place X
        if row < m and board[row][col] == ' ':  
            return Place_And_Check_Move(row, col)
            
        # Check up
        row = input_row # Reset row to input_row for up check
        while row >= 0 and board[row][input_col] == 'O':
            row -= 1
        # If the calculated spot is within bounds (row >= 0) and empty, place X
        if row >= 0 and board[row][input_col] == ' ':
            return Place_And_Check_Move(row, col)

    # --- Right Diagonal Blocking Logic ---
    elif max_pos == Right_Diagonal_check(input_row, input_col, 'O'):
        # Check down and right
        row = input_row
        col = input_col
        # Use 'm' and 'n' for boundary check
        while row < m and col < n and board[row][col] == 'O':
            col += 1
            row += 1
        # If the next spot is within bounds and empty, place X
        if row < m and col < n and board[row][col] == ' ':
            return Place_And_Check_Move(row, col)
            
        # Check up and left
        row = input_row # Reset row to input_row
        col = input_col # Reset col to input_col
        while col >= 0 and row >= 0 and board[row][col] == 'O':
            col -= 1
            row -= 1
        # If the calculated spot is within bounds and empty, place X
        if col >= 0 and row >= 0 and board[row][col] == ' ':
            return Place_And_Check_Move(row, col)

    # --- Left Diagonal Blocking Logic ---
    elif max_pos == Left_Diagonal_check(input_row, input_col, 'O'):
        # Check up and right 
        row = input_row
        col = input_col
        # Use 'n' and row >= 0 for boundary check
        while row >= 0 and col < n and board[row][col] == 'O':
            col += 1
            row -= 1
        # If the next spot is within bounds and empty, place X
        if row >= 0 and col < n and board[row][col] == ' ':
            return Place_And_Check_Move(row, col)
            
        # Check down and left
        row = input_row # Reset row to input_row
        col = input_col # Reset col to input_col
        while col >= 0 and row < m and board[row][col] == 'O':
            col -= 1
            row += 1
        # If the calculated spot is within bounds and empty, place X
        if col >= 0 and row < m and board[row][col] == ' ':
            return Place_And_Check_Move(row, col)
        
    # If no blocking move found, make a random move
    return Smart_Random_Move()

def Smart_Random_Move():
    'function Smart_Random_Move() makes a random move for the smart machine if no blocking move is found'
    import random
    x = random.randrange(1, m+1)
    y = random.randrange(1, n+1)
    while board[x-1][y-1] != ' ':
        x = random.randrange(1, m+1)
        y = random.randrange(1, n+1)
    
    row = x - 1
    col = y - 1
    Place_And_Check_Move(row, col)
    

def Machine_Turn(option):
    'This function is complete here'
    if(option=='1'):
        return(Random_Machine_Turn())
    elif option=='2':
        return(Smart_Machine_Turn())
    else:
        print('Error')
    Print_Board()

#Global Variables
while True: #use try and except to make sure user inputs valid m and n values
    try:
        m = input('Input the number of rows that you want: (1-10) ')
        m = int(m)
        if m in range(1, 11):
            break
        elif m not in range(1, 11):
            print('Wrong Input.')
    except:
        print('Wrong Input.')
while True:
    try:
        n = input('Input the number of columns that you want: (1-10) ')
        n = int(n)
        if n in range(1, 11):
            break
        elif n not in range(1, 11):
            print('Wrong Input.')
    except:
        print('Wrong Input.')
board = [[' ']*n for i in range(m)]

Print_Board()
while True:
    try:
        option = input('What machine would you like to play with? (1. Random) or (2. Smart): ')
        if option == '1' or option == '2':
            break
        else:
            print('Wrong input. Please choose between 1 and 2 as an option.')
    except:
        print('Wrong input. Please choose between 1 and 2 as an option.')

while(True):
    winner = Human_Turn()
    if(winner==True):
        print('***********************\nCONGRATULATIONS!!! Human Win!!!\n***********************')
        break
    if(All_Spots_Chosen()):
        print('***********************\nNo more spots left. Game Ended.***************')
        break

    wait = ''
    while wait != 'c':
        wait = input('Press \'c\' to continue for the computer\'s turn: ')

    winner = Machine_Turn(option)

    if(winner==True):
        print('***********************\nCONGRATULATIONS!!! Computer Win!!!\n***********************')
        break

    if(All_Spots_Chosen()):
        print('***********************\nNo more spots left. Game Ended.***************')
        break