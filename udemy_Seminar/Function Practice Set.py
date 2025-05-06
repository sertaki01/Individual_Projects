def is_even(x):
    return x % 2 == 0
   
def slugify(phrase):
    return phrase.strip().lower().replace(" ","-")

def count_vowels(phrase):
    count = 0
    for char in phrase:
        if char in ("aeiou"):
            count += 1
    return count

