from hands import get_random_hand, hand_text, get_hand_img
from pick import pick
import os


def check_winner(player, pc):
    # draw
    if player == 'rock' and pc == 'rock' or \
        player == 'paper' and pc == 'paper' or \
        player == 'scissors' and pc == 'scissors':
        return 0
    # player wins
    elif player == 'rock' and pc == 'scissors' or \
        player == 'paper' and pc == 'rock' or \
        player == 'scissors' and pc == 'paper':
        return 1
    else:  # pc wins
        return -1


def reset():
    os.system('cls' if os.name == 'nt' else 'clear')


def play():
    # player turn
    player_option, player_index = \
        pick(hand_text, "Que mano eliges?", indicator='=>')
    print(f"Elegiste: {player_option}")
    print(get_hand_img(player_index))

    # PC turn
    pc_choice = get_random_hand()
    print(f"Tu rival eligió: {pc_choice['text']}")
    print(pc_choice['img'])

    # Result
    result = check_winner(player_option, pc_choice['text'])

    if result == 0:
        print("Es un empate!")
    elif result == 1:
        print("Has ganado!")
    else:
        print("Has perdido...")
