"""i am going to list here all the things i need"""
# board
# display board
# play game
# handle turn
# check winner
# check row
# check column
# check diagonal
# check tie
# flip player

# global Variable
winner = None

game_is_not_over = True

current_player = "X"

# first of all, the board (we can say that it's up to you to choose your board's type).
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# now, let's display it.
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# main part of the game, play game
def play_game():
    # it's obvious that we display first, right?
    display_board()

    global game_is_not_over

    while game_is_not_over:

        handle_turn(current_player)

        check_if_game_is_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(str(winner) + " won.")

    elif winner is None:
        print("Tie")


# now that we have the board, the next thing to do is to handle turn
def handle_turn(player):

    not_valid = True
    print(player + "'s turn.")

    # There may a case that the person who plays input something weird. how are you going to handle that
    # i am going to say here, 1-9. you know why
    position = input("Choose one position from 1-9: ")

    while not_valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("wrong input, go again!")
            position = input("Choose one position from 1-9: ")

        # now we are going to clear things up
        position = int(position) - 1

        # display it on the board
        if board[position] == "-":
            not_valid = False

        else:
            print("you can't go there")

    board[position] = player

    display_board()


def check_if_game_is_over():
    # what would be the reason of this: someone won or it's tie
    check_for_winner()
    check_if_tie()


# now we are going to create one function for each of these option


def check_for_winner():
    global winner
    # everyone knows the rule. so, let's check each case that may happen
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None


# and again, walk through each option
def check_rows():
    global game_is_not_over

    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        game_is_not_over = False

    if row1:
        return board[0]

    elif row2:
        return board[3]

    elif row3:
        return board[6]


def check_columns():
    global game_is_not_over

    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    if column1 or column2 or column3:
        game_is_not_over = False

    if column1:
        return board[0]

    elif column2:
        return board[1]

    elif column3:
        return board[2]


def check_diagonals():
    global game_is_not_over

    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    if diagonal1 or diagonal2:
        game_is_not_over = False

    if diagonal1:
        return board[0]

    elif diagonal2:
        return board[2]


def check_if_tie():

    global game_is_not_over

    if "-" not in board:
        game_is_not_over = False

    return


# finally, build the function that make sure that each player go by turn.
def flip_player():

    global current_player

    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"

    return


play_game()
