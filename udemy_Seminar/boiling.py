unit = input("What unit are you using(f = Fahrenheit, c = Celsius, k = Kelvin)? ")

temp = float(input("What temperature is the water? "))

if unit == "f":
    if temp >= 212:
        print("The water is boiling!!")
    else:
        print("The water is not boiling, must hit 212  Fahrenheit")
elif unit == "c":
    if temp >= 100:
        print("The water is boiling!!")
    else:
        print("The water is not boiling, must hit 100 Celsius")
elif unit == "k":
    if temp >= 373:
        print("The water is boiling!!")
    else:
        print("The water is not boiling, must hit 373 Kelvin")
else:
    print("I dont any idea what are you takling about sorry :(")