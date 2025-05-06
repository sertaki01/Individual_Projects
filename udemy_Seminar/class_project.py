class human:

    species = "Homo sapiens"

    def __init__(self, name, height, country):
        self.name = name
        print("\nHeight in cm please :).\n")
        self.height = height
        self.country = country
        self.languages = set()

    def language(self, *new_language):
        for lan in new_language: 
            self.languages.add(lan)

    @classmethod
    def unknown(cls):
        return cls("unknown", "unknown", "unknown")

class Animals(human):
    def __init__(self, name, height, country, favorite_animal):
        super().__init__(name, height, country)
        self.favorite_animal = favorite_animal
        
Jim = human("Jim", 181, "Greece")

print(Jim.name, Jim.height, Jim.country, sep = "\n")

Jim.language("Greek", "English")

print(Jim.languages)

print(Jim.species)

Athanasia = human.unknown()

print(Athanasia.name, Athanasia.height, Athanasia.country, Athanasia.languages, Athanasia.species, sep ="\n")

Stelios = Animals("Stelios", 190, "Albania", "Dog")

print(Stelios.name, Stelios.height, Stelios.country, Stelios.languages, Stelios.species, Stelios.favorite_animal, sep = "\n")
