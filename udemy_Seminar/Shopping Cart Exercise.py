print("""WELCOME TO OUR USELESS STORE!
*****************************""")

item = input("What item are you purchasing? ")

price = float(input(f"what is the price of {item}? "))

quantity = int(input(f"How many {item}(s) are you buying? "))

print(f"\nAdded {quantity} {item}(s) to shopping card")

print(f"Subtotal: ${price * quantity}\n")