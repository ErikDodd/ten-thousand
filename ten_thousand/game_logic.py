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
        #print("tuple", tuple)
        count_dict = Counter(tuple)
        score_counter = 0

        if len(count_dict) == 6:
            return 1500

        if len(count_dict) == 3 and all(value == 2 for value in count_dict.values()):
            return 1500

        for number, count in count_dict.items():
            number_to_int = int(number)
            #print(f"Number_type: {type(number)}")
            #print(f"Count: {count}")
            if count < 3:
                #print(f"dice_points: {dice_points}")
                score_counter += count * dice_points.get(number_to_int, 0)
            elif count == 3:
                score_counter += triple_points[number_to_int]
            elif count == 4:
                score_counter += triple_points[number_to_int] * 2
            elif count == 5:
                score_counter += triple_points[number_to_int] * 3
            elif count == 6:
                score_counter += triple_points[number_to_int] * 4

        return score_counter
