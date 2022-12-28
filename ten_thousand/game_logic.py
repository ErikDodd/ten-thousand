from random import randint
from collections import Counter

dice_points = {1: 100, 5: 50}
triple_points = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}


class GameLogic:

    @staticmethod
    def roll_dice(num_dice):
        values = []
        for i in range(num_dice):
            value = randint(1, 6)
            values.append(value)
        return tuple(values)

    @staticmethod
    def calculate_score(tuple):
        count = Counter(tuple)
        score_counter = 0


        # Score for Straights
        if len(count) == 6:
            return 1500

        # Three Pair
        if len(count) == 3 and all(value == 2 for value in count.values()):
            return 1500


        for number, count in count.items():
            if count < 3:
                score_counter += count * dice_points.get(number, 0)
            elif count == 3:
                score_counter += triple_points[number]
            elif count == 4:
                score_counter += triple_points[number] * 2
            elif count == 5:
                score_counter += triple_points[number] * 3
            elif count == 6:
                score_counter += triple_points[number] * 4

        return score_counter




        # for dice in count:
        # GameLogic.dice_points[dice]
