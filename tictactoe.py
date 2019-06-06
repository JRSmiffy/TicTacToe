
# # # # # Tic Tac Toe Game

# # # Rules

# There are two players
# Player 1 enters their name and selects their token
# Player 2 enters their name and selects their token
# The Game begins
# Players take it in turns positioning their tokens on a 3 x 3 grid
# The grid is represented by a numbers 1 - 9 in the following way:
# 0 1 2
# 3 4 5
# 6 7 8
# The game end with a tie if the whole grid is filled or
# when a player gets 3 in a row, column or diagonal

# 1 - The Players receive the Rules
print("\n\nHere be the Rules:\n")
print("Player 1 enters their name and selects their token\n")
print("Player 2 enters their name and selects their token\n")
print("The Game begins\n")
print("Players take it in turns positioning their tokens on a 3 x 3 grid\n")
print("The grid is represented by a numbers 1 - 9 in the following way:\n")
print("0 1 2")
print("3 4 5")
print("6 7 8\n")
print("A player wins if they gets 3 in a row, column or diagonal or\n")
print("the game ends with a tie if the whole grid is filled\n\n")

# 2 - The Players enter their names and select their token
name1 = input("Welcome Player 1, what is your name?\n")
name2 = input("Welcome Player 2, what is your name?\n")
token2 = input("\nHi {}, as {} gets to go first, which token would you like? x or o\n".format(name2, name1))
if token2 == 'x':
    print("\n{}, you are x's\n".format(name2))
    print("{}, you are o's\n".format(name1))
    token1 = 'o'
elif token2 == 'o':
    print("\n{}, you are o's\n".format(name2))
    print("{}, you are x's\n".format(name1))
    token1 = 'x'
else:
    token2 = 'x'
    print("\nAs you couldn't choose properly {}, you are x's\n".format(name2))
    print("{} you are o's\n".format(name1))
    token1 = 'o'

print("\nLet battle commence!\n")

# 3 - Actual game logic
board = ['_', '_', '_',
         '_', '_', '_',    # Empty board initialized
         '_', '_', '_']

def print_board(current_board): # print out the board
    print("\n")
    print(str(current_board[0]) + "   " + str(current_board[1]) + "   " + str(current_board[2]))
    print(str(current_board[3]) + "   " + str(current_board[4]) + "   " + str(current_board[5]))
    print(str(current_board[6]) + "   " + str(current_board[7]) + "   " + str(current_board[8]))
    print("\n")

def check_win(current_board, token, rem_pos): # checks whether winning conditions have been met
    # Check rows
    if [current_board[0], current_board[1], current_board[2]].count(token) == 3:
        return("Win")
    if [current_board[3], current_board[4], current_board[5]].count(token) == 3:
        return("Win")
    if [current_board[6], current_board[7], current_board[8]].count(token) == 3:
        return("Win")
    # Check cols
    if [current_board[0], current_board[3], current_board[6]].count(token) == 3:
        return("Win")
    if [current_board[1], current_board[4], current_board[7]].count(token) == 3:
        return("Win")
    if [current_board[2], current_board[5], current_board[8]].count(token) == 3:
        return("Win")
    # Check diagonal
    if [current_board[0], current_board[4], current_board[8]].count(token) == 3:
        return("Win")
    if [current_board[2], current_board[4], current_board[6]].count(token) == 3:
        return("Win")
    if rem_pos == []:
        return("Tie")


print_board(board)
print("\n")

rem_pos = ["0", "1", "2", "3", "4", "5", "6", "7", "8"] # This will track which positions are available to avoid overwritting
while 1 == 1: # Intentional infinite loop that we'll break out of when the time is right
    # Player 1's move
    move_success = False
    while move_success == False:
        pos = input("{}, enter a number between 0 - 8 to place an {} in the position you want\n".format(name1, token1))
        if pos in rem_pos:
            rem_pos.remove(pos)
            move_success = True

    # Update board
    board[int(pos)] = token1
    # Print board
    print_board(board)
    if check_win(board, token1, rem_pos) == "Win":
        print("\nCongrats {}, you won!".format(name1))
        break
    elif check_win(board, token1, rem_pos) == "Tie":
        print("\nThat's it ladies and gents, we have a tie!")
        break

    # Player 2's move
    move_success = False
    while move_success == False:
        pos = input("{}, enter a number between 0 - 8 to place an {} in the position you want\n".format(name2, token2))
        if pos in rem_pos:
            rem_pos.remove(pos)
            move_success = True

    # Update board
    board[int(pos)] = token2
    # Print board
    print_board(board)
    # Check Win
    if check_win(board, token2, rem_pos) == "Win":
        print("\nCongrats {}, you won!".format(name2))
        break
    elif check_win(board, token1, rem_pos) == "Tie":
        print("\nThat's it ladies and gents, we have a tie!")
        break




#
