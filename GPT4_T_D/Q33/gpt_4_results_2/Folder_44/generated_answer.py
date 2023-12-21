
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    subset = string[46:49]
    return [char for char in subset if char in vowels and 'p' >= char > '[']
