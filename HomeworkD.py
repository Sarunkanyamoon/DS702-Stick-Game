import random

def play_game():
    sticks = int(input("How many sticks (N) in the pile: "))
    print("There are", sticks, "sticks in the pile.")
    name = input("What is your name: ")

    for _ in range(sticks):
        while True:
            player_choice = int(input(name + ", how many sticks will you take (1 or 2): "))
            if player_choice in [1, 2]:
                break
            else:
                print("Invalid input. Please choose 1 or 2.")

        sticks -= player_choice
        print("There are", sticks, "stick(s) in the pile.")

        if sticks <= 0:
            print(name, "takes the last stick.")
            print("I, smart computer, win !!!!")
            break

        smart_computer = random.randint(1, 2)
        print("I, smart computer,", "take:", smart_computer)
        sticks -= smart_computer
        print("There are", sticks, "stick(s) in the pile.")

        if sticks <= 0:
            print("I, smart computer, take the last stick.")
            print(name, "win (I, smart computer, am sad T_T)")
            break
        

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break