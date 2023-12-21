
def return_vowels(string):
    vowels = 'aeiouAEIOU'
    result = [character for character in string[55:65] if character in vowels and 'Z' < character <= 'w']
    return result
