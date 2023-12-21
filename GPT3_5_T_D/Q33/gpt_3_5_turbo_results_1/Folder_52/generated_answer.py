
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in string[24:68]:
        if 'f' < letter <= '|':
            if letter.lower() in vowels:
                result.append(letter)
    return result
