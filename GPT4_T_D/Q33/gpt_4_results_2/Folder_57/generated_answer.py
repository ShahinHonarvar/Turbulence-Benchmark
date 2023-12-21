
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string_portion = string[21:23]
    result = [char for char in string_portion if char in vowels and '-' < char <= 'n']
    return result
