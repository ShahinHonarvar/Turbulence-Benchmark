
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    char_check = [char for char in s[2:7] if char >= '^' and char <= 'd']
    return [char for char in char_check if char in vowels]
