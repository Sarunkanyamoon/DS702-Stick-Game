# HW1D_SticksInThePile_GAME_START
# Created on 18 July 2023 16:59
# Created by Sarun Kanyamoon studentID:660631099

import random
# Add fuction random before define play game condition.

def play_game():
    sticks = int(input("How many sticks (N) in the pile: "))
    print("There are", sticks, "sticks in the pile.")
    name = input("What is your name: ")

    # Create condition to take out stick in the range that our define.
    while sticks > 0:
    # Create loop condition of code until sticks in the pile <= 0.
        for _ in range(sticks):
            while True:
                player_choice = int(input(name + ", how many sticks will you take (1 or 2): "))
                if player_choice in [1, 2]:
                # This if condition determine player to pick stick in range 1-2.
                    break
                else:
                    print("Invalid input. Please choose 1 or 2.")
            # The sticks that player pick will use to minus in the pile from this function.
            sticks -= player_choice
            print("There are", sticks, "sticks in the pile.")
            # If the stick <= 0 on this stage Bot will win the game.
            if sticks <= 0:
                print(name, "takes the last stick.")
                print("I, smart computer, win !!!!")
                return False
            # Use random.randint to make Bot random select sticks from in pile in range 1-2.
            smart_computer = random.randint(1, min(2, sticks))
            print("I, smart computer, take:", smart_computer)
            sticks -= smart_computer
            print("There are", sticks, "sticks in the pile.")
            
            # If the stick <= 0 on this stage Player will win the game.
            if sticks <= 0:
                print("I, smart computer, take the last stick.")
                print(name, "win (I, smart computer, am sad T_T)")
                return False

    return True

play_game()