
def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    subset = s[90:97]
    return [letter for letter in subset if letter in vowels and '_' < letter <= 'x']
