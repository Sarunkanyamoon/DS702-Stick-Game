# SticklnThePileGame
# Created on 17:34 Saturday 8 July 2023
# Created by Sarun Kanyamoon studentID:660631099

# Define While loop uuse for helpping loop of calculate condition.
while True:
    # Use int(input) to take integer data for number of sticks in the pile.
    sticks = int(input("How many sticks (N) in the pile: "))
    print("There are", sticks, "sticks in the pile.")
    name = input("What is your name: ")
    n = 0
    # Define n variable to stocked value of how many times we use to take sticks out.
    
    # Create While condition to loop the calculation and define there condition step.
    while sticks > 0:
        # Create R variable to stocked int(input) data of user how many sticks that they want.
        R = int(input(name + ", how many sticks will you take (1 or 2): "))
        # Define if/else/elif condition play with R variable.
        if R > 0 and R <= 2:
            if R > sticks:
                print("There are not enough sticks to take.")
            else:
                # Determine equation for calculate number of sticks.
                sticks -= R
                # Define n variable condition here to keepp data of counting round when sticks in the pile was took out.
                n += 1
                print("There are", sticks, "sticks in the pile.")
        # Define Others condition when user insert number of sticks not match with above condition.
        elif R > 2:
            print("No you cannot take more than 2 sticks!")
        else:
            print("No you cannot take less than 1 stick!")

    print("OK.There is no stick left in the pile.""You spent", n,"times.")
    # Use Break command for determine end of loop.
    break

