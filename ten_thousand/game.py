from game_logic import GameLogic
from collections import Counter


class Banker:
    def __init__(self, balance=0, shelved=0):
        self.balance = balance
        self.shelved = shelved

    def shelf(self):
        pass

    def bank(self):
        self.balance += self.shelved
        self.shelved = 0
        return self.balance

    def clear_shelf(self):
        pass


class Game:

    def __init__(self, points=0):
        self.round = 1
        self.banker = Banker()
        self.dice_amount = 6
        self.points = points


    def start_game(self, current_dice_roll=GameLogic.roll_dice):
        print("""
Welcome to Ten Thousand
(y)es to play or (n)o to decline
        """)
        user_response = input("> ")
        if user_response == "n":
            print("OK. Maybe another time")
        elif user_response == "y":
            self.play(current_dice_roll)

    def play(self, current_dice_roll):
        while True and self.points > -1 and self.banker.balance < 10000:
            print(f"round {self.round}")
            print(f"Rolling {self.dice_amount} dice...")
            dice_results = current_dice_roll(self.dice_amount)
            dice_string = ""
            for numbers in dice_results:
                dice_string += f"{numbers} "
            print(f"*** {dice_string} ***")
            print("Enter dice to keep, (r)oll again, (b)ank your points  or (q)uit:")
            enter_dice = input("> ")
            if len(enter_dice) < self.dice_amount:
                #print(f"{enter_dice}")
                #print(f"{type(enter_dice)}")
                if enter_dice == "q":
                    print(f"Thanks for playing. You earned {self.banker.balance} points")
                    return False
                elif (enter_dice == "b") or (enter_dice == "r"):
                    #print(f"User Input: {enter_dice}")
                    self.banker.balance += self.points
                    #print(f"Total points: {self.banker.balance}")
                    self.round = self.round + 1
                    self.dice_amount = 6
                    self.points = 0
                    #print(f"Round: {self.round}, Dice Amount: {self.dice_amount}, Points: {self.points}")

                #elif enter_dice != "q" or enter_dice != "b" or enter_dice != "r":
                else:
                    cheater = False
                    while not cheater:
                        dice_string_dict = Counter(dice_string)
                        for i in enter_dice:
                            if not dice_string.count(i) or dice_string_dict[i] < 0:
                                print("Cheater!!! Or possibly made a typo...")
                                cheater = True
                            elif dice_string_dict[i] > 0:
                                #print("this was in the dictionary", i)
                                #print(type(i))
                                #int_i = int(i)
                                #print(f"dictionary before: {dice_string_dict}")
                                dice_string_dict[i] -= 1
                                #if dice_string_dict[i] < 0:
                                    #print("Cheater!!! Or possibly made a typo...")
                                    #cheater = True
                                #print(f"dictionary after: {dice_string_dict}")


                        #dice_string enter_dice
                        #print(len(enter_dice))
                        new_points = 0
                        if not cheater:
                            new_points = GameLogic.calculate_score(enter_dice)
                        #print(new_points)
                        self.points += new_points
                        #print(f"Round points: {self.points}")
                        self.dice_amount = self.dice_amount - len(enter_dice)
                        #print("dice amount after: ", self.dice_amount)
                        print(f"""
    You have {self.points} unbanked points and {self.dice_amount} dice remaining
    (r)oll again, (b)ank your points or (q)uit:""")
                        cheater = True





if __name__ == "__main__":
    game = Game()
    game.start_game()
