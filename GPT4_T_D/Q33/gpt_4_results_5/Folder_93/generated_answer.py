
def return_vowels(string):
    vowels = ['A', 'E', 'I', 'O', 'U','a', 'e', 'i', 'o', 'u']
    string_range = string[54:82]
    vowels_in_range = [char for char in string_range if char >= '=' and char <= '@' and char in vowels]
    return vowels_in_range
