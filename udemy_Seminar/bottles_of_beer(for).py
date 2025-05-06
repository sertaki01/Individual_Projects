for bottles_of_beer in range(99,0,-1):
    
    print(f"{bottles_of_beer} bottles of beer on the wall.\n{bottles_of_beer} bottles of beer.")

    if bottles_of_beer > 1:   
        print(f"Take one down, pass it around, {bottles_of_beer - 1} bottles of beer on the wall")
    else:
        print("Take one down, pass it around, no more bottles of beer on the wall")

    print("*" * 45)

        

    
