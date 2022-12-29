from game_logic import GameLogic


class Banker:
    def __init__(self, balance=0, shelved=0):
        self.balance = balance
        # unbanked points
        self.shelved = shelved
        pass

    def shelf(self, points):
        self.points = points
        pass

    def bank(self):
        self.balance += self.shelved
        self.shelved = 0
        return self.balance

    def clear_shelf(self):
        pass


class Game:

    def __init__(self):
        self.round = 0
        self.banker = Banker()
        self.dice_amount = 6

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
        while True:
            self.round = self.round + 1
            print(f"Starting round {self.round}")
            print(f"Rolling {self.dice_amount} dice...")
            dice_results = current_dice_roll(self.dice_amount)
            dice_string = ""
            for numbers in dice_results:
                dice_string += f"{numbers} "
            print(f"*** {dice_string} ***")
            print("Enter dice to keep, or (q)uit:")
            enter_dice = input("> ")
            if enter_dice == "q":
                print(f"Thanks for playing. You earned {self.banker.balance} points")
                return False

            # elif print(f"""
            # You have 50 unbanked points and 5 dice #remaining
            # (r)oll again, (b)ank your points or (q)uit:
            # """):


if __name__ == "__main__":
    game = Game()
    game.start_game()
