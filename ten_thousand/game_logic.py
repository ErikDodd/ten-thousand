from random import randint


class GameLogic:

    @staticmethod
    def roll_dice(num_dice):
        values = []
        for i in range(num_dice):
            value = randint(1, 6)
            values.append(value)
        return tuple(values)
