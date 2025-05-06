from random import randint

roll_1 = randint(1,6)

roll_2 = randint(1,6)

i = 1

while not roll_1 == 1 or roll_2 != 1:

    print(f"roll_1 = {roll_1}\troll_2 = {roll_2}")

    roll_1 = randint(1,6)

    roll_2 = randint(1,6) 

    i += 1

print(f"roll_1 = {roll_1}\troll_2 = {roll_2}, Hey we got snakes eyes finally\nWe made it after {i} trials")