
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[23:75] if char in vowels and char > 'L' and char <= 'd']
