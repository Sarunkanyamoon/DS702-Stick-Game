# HW1E_SticksInThePile+AI
# Created on 25 July 2023 18:39
# Created by Sarun Kanyamoon studentID:660631099
# Create and split the loop in to more def function from previous Homework.

import random
# Create of play_game function to take input of player name.
def play_game():
    #Annouce variable in to global.
    global sticks, name, max_choice
    sticks = int(input("How many sticks (N) in the pile: "))
    max_choice = min(2, sticks)
    name = input("What is your name: ")
    print("There are", sticks, "sticks in the pile.")

# Create player_turn function to define condition of sticks that they can take.
def player_turn():
    global sticks, name, max_choice
    player_choice = int(input("how many sticks you will take (1 or {max_choice}): "))
    # Define condition of player picking sticks.
    if player_choice in [1, 2] and player_choice <= sticks: 
        sticks -= player_choice
        print("There are", sticks, "sticks in the pile.")    
    else:
        print("Invalid input. Please choose 1 or 2.")
        return player_turn()
    if sticks <= 0:
        print("You takes the last stick.")
        print("I WON (Python WON)")
# Create computer_turn function.   
# Computer's turn calculate the number of sticks to leave the player with to guarantee a win.
def computer_turn():
    global sticks, name, computer_choice
    # If the remaining sticks are a multiple of 3, choose 2 sticks. Otherwise, choose 1 stick.
    computer_choice = 2 if sticks % 3 == 0 else 1

    sticks -= computer_choice
    print("I take", computer_choice,"stick, there are", sticks, "sticks in the pile")

    if sticks <= 0:
        print("I, smart computer, take the last stick.")
        print(name, "wins (I, smart computer, am sad T_T)")
   

# Call the function that I create on above and loop the function with " While" condition.
play_game()
while sticks > 0:
    computer_turn()
    player_turn()