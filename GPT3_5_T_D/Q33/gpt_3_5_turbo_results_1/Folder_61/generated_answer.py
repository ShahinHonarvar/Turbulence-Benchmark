
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    characters = list(string)[1:4]
    return [char for char in characters if 'C' < char <= 'I' and char in vowels]
