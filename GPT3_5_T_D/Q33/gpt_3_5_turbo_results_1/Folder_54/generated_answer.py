
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for character in string[23:85]:
        if character in vowels and 'W' < character <= 'v':
            result.append(character)
    return result
