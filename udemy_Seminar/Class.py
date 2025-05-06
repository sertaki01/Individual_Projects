class adoption:

    species = "Canis familiaris"
    num_dogs = 0

    def __init__(self,sex,name,breed):
        while not (sex == "female" or sex == "male" or sex == "unknown"):
            sex = input("You have two options for gender: male or female: ")
        self.sex = sex
        self.name = name
        self.breed = breed
        self.tricks = set()
        adoption.num_dogs += 1

    @classmethod
    def record(cls):
         return cls("unknown", "unknown", "unknown")

    def add_tricks(self, *trick):
            for i in range(len(trick)):
                 self.tricks.add(trick[i])

class lion(adoption):
     
    def roar(self):
        print(f"{self.name} roars !!!") 

    def __init__(self,sex,name,breed):
         super().__init__(sex,name,breed)

rocky = adoption("male" ,"rocky" , None)

print(f"sex = {rocky.sex}", f"name = {rocky.name}" ,f"breed = {rocky.breed}" ,f"tricks = {rocky.tricks}", f"species = {rocky.species}" , sep = "\n")

rocky.add_tricks("gentle", "roll")

print(f"rocky_tricks = {rocky.tricks}")

remi = adoption("female", "remi", "pug")

remi.add_tricks("roll")

print(f"remi_tricks = {remi.tricks}")

print(adoption.num_dogs)

milo = adoption.record()

print(milo.sex, milo.name, milo.breed, sep = "\n")

Cat = lion("male", "Lucky", "Lion")

Cat.add_tricks("baby voice")

Unknown_cat = lion.record()

print("\n"+ Unknown_cat.name)

print(Cat.name, Cat.breed, Cat.sex, Cat.tricks, sep = "\n")

jerry = lion("male", "jerry", None)

print(jerry.sex, jerry.name, jerry.breed, jerry.tricks, sep = "\n")

jerry.roar()
