from random import randint

dice_number = int(input("How many dice are we rolling? "))

sides_number = int(input("How many sides on each die? "))

reply = None

while (dice_number < 1 or dice_number > 20) or (sides_number < 1 or sides_number > 20):
    
    dice_number = int(input("How many dice are we rolling? "))

    sides_number = int(input("How many sides on each die? ")) 
    
while True:

    line = "|"

    for roll in range(dice_number):

        char = f"{randint(1,sides_number)}|"

        line += char

    print(line)

    reply = input("Roll again? ('q' to quit) ")

    if reply == "q":
        break
