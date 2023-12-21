
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in string[69:82]:
        if letter in vowels and '[' < letter <= '~':
            result.append(letter)
    return result
