# main.py

import random
from game.game_logic import GameLogic
from utils.validation import validate_input


def main():
    player_name = validate_input("Введите имя вашего героя: ", str)
    computer_names = ["Артемий", "Василий", "Глеб"]
    computer_name = random.choice(computer_names)

    game = GameLogic(player_name, computer_name)
    game.start()


if __name__ == "__main__":
    main()