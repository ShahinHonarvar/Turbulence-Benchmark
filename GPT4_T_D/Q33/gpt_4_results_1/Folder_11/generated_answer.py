
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    substring = string[29:73]
    result = [char for char in substring if char in vowels and '#' < char <= '(']
    return result
