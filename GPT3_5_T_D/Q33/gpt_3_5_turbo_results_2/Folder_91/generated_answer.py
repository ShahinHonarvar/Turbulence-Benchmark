
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in string[4:8] if c > 'P' and c <= 'r' and c.lower() in vowels]
