
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    substr = string[837:975]
    res = [letter for letter in substr if letter in vowels and 'N' < letter <= 'W']
    return res
