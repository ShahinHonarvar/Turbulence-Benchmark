
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in string[90:97] if char in vowels and '_' < char <= 'x']
