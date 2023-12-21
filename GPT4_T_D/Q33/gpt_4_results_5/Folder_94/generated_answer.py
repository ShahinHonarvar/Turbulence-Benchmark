
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    letters = string[40:94]
    return [char for char in letters if char in vowels and '4' < char <= 'H']
