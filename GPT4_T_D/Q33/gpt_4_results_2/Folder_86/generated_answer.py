
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[273:275] if char in vowels and '+' < char <= 'o']
