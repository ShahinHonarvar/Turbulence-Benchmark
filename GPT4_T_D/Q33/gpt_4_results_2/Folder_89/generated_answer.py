
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    subset = string[50:51]
    result = [char for char in subset if char in vowels and ',' < char <= 'v']
    return result
