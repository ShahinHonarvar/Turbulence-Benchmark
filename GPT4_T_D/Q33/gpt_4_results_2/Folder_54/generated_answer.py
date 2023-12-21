
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    substring = string[23:85]
    return [char for char in substring if char in vowels and 'W' < char <= 'v']
