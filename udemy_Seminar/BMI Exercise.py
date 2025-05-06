height = float(input("Enter your height in inches: "))

weight = float(input("Enter your weight in pounds: "))

bmi = round(weight * 703 / height ** 2, 2)

message = f"Your BMI of {bmi} makes you"

if bmi <= 16:
    print(f"{message} Severely Underweight ")
elif bmi <= 18.4:
    print(f"{message} Underweight")
elif bmi <= 24.9:
    print(f"{message} Normal")
elif bmi <= 29.9:
    print(f"{message} Overweight")
elif bmi <= 34.9:
    print(f"{message} Moderately Obese")
elif bmi <= 39.9:
    print(f"{message} Severely Obese")
else:
    print(f"{message} Morbidly Obese")