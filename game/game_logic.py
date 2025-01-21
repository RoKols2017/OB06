# game/game_logic.py

from .hero import Hero


class GameLogic:
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        while self.player.is_alive() and self.computer.is_alive():
            print(f"{self.player.name} атакует {self.computer.name}")
            self.player.attack(self.computer)
            print(f"Здоровье {self.computer.name}: {self.computer.health}")

            if not self.computer.is_alive():
                break

            print(f"{self.computer.name} атакует {self.player.name}")
            self.computer.attack(self.player)
            print(f"Здоровье {self.player.name}: {self.player.health}")

        winner = self.player if self.player.is_alive() else self.computer
        print(f"Победитель - {winner.name}")