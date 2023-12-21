
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[63:79] if char > 'D' and char <= 'y' and char.lower() in vowels]
