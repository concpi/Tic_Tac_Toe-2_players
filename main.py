
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

legal_inputs = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def clear_board():
    return [" ", " ", " "," ", " ", " ", " ", " ", " "]


def current_player(rnd):
    player_sign = "O"

    if rnd % 2 == 0:
        player_sign = "X"

    return player_sign


def draw_board():
    print(f" {board[0]} | {board[1]} | {board[2]}\n"
          f"-----------\n"
          f" {board[3]} | {board[4]} | {board[5]}\n"
          f"-----------\n"
          f" {board[6]} | {board[7]} | {board[8]}\n")


def check_for_win(player):

    if (board[0] == board[1] and board[1] == board[2] and board[0] != " "
            or board[3] == board[4] and board[4] == board[5] and board[3] != " "
            or board[6] == board[7] and board[7] == board[8] and board[6] != " "
            or board[0] == board[4] and board[4] == board[8] and board[0] != " "
            or board[2] == board[4] and board[4] == board[6] and board[2] != " "
            or board[0] == board[3] and board[3] == board[6] and board[0] != " "
            or board[1] == board[4] and board[4] == board[7] and board[1] != " "
            or board[2] == board[5] and board[5] == board[8] and board[2] != " "):
        print(f"Player {player} wins!\n")
        draw_board()
        return True


def play(player):
    choice = input("Play by choosing a number from 1-9: ")

    while choice not in legal_inputs:
        choice = input("Please choose a number from 1-9 only: ")

    choice = int(choice) - 1

    while board[choice] != " ":
        choice = int(input("Choose an empty field: ")) - 1

    board[choice] = player
    clear()


def new_game():

    game_is_on = True
    round_nr = 0

    while game_is_on:
        player = current_player(round_nr)

        print(f'Current player: "{player}"\n')
        draw_board()

        play(player)

        if check_for_tie():
            game_is_on = False

        if check_for_win(player):
            game_is_on = False

        round_nr += 1


def check_for_tie():
    if " " not in board:
        print("TIE\n")
        draw_board()
        return True


def clear():
    print("\n" * 10)

##################################################


new_game()

next_game = input("New game? (y/n): ")
if next_game == "y":
    board = clear_board()
    clear()
    new_game()
