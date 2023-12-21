
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    character_range = s[32:97]
    vowels_in_range = [letter for letter in character_range if letter in vowels and 'Q' < letter <= ']']
    return vowels_in_range
