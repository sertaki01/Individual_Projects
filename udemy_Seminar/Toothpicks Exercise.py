player_1 = input("enter players 1's name: ")

player_2 = input("\nenter players 2's name: ")

toothpicks_left = 13

while True:
    for player in (player_1, player_2):

        print("\n" + "| " * toothpicks_left)
        
        print(f"There are {toothpicks_left} toothpicks left")
 
        toothpicks = int(input(f"How many do you take, {player} ?\n"))

        while toothpicks > 3 or toothpicks < 1:

             toothpicks = int(input(f"\nYou can only chose 1,2, or 3: \n")) 

        toothpicks_left -= toothpicks

        if toothpicks_left < 1:

            print(f"\n{player} wins!!!")

            print("GAME OVER!!\n")

            break

    if toothpicks_left < 1:
        
        break 
    
