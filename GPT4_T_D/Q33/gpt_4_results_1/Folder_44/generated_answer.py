
def return_vowels(string):
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    chars = string[46:49]
    return [char for char in chars if char in vowels_list and (char > '[' and char <= 'p')]
