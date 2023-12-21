
def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    substring = str[44:95]
    valid_characters = [char for char in substring if char in vowels and '5' < char <= '<']
    return valid_characters
