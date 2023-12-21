
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    substring = string[2:7]
    vowels_in_range = [char for char in substring if char in vowels and '^' < char <= 'd']
    return vowels_in_range
