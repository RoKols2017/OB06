# game/hero.py

import random


class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.base_attack_power = 20

    def attack(self, other):
        if not isinstance(other, Hero):
            raise TypeError("Можно атаковать только другого героя")

        # Генерируем случайное значение силы удара в пределах от 30% до 100%
        attack_power = int(self.base_attack_power * random.uniform(0.3, 1))

        other.health -= attack_power

    def is_alive(self):
        return self.health > 0