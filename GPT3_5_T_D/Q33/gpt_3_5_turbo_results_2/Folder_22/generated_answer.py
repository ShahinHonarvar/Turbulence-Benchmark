
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in string[56:90]:
        if letter > 'K' and letter <= 'z' and letter in vowels:
            result.append(letter)
    return result
