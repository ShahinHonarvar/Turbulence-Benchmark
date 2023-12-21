
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    substring = string[21:23]
    result = []
    for letter in substring:
        if letter > '-' and letter <= 'n' and letter in vowels:
            result.append(letter)
    return result
