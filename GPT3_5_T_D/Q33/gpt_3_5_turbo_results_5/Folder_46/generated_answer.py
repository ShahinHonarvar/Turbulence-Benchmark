
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[10:83] if '%' < char <= 'e' and char in vowels]
