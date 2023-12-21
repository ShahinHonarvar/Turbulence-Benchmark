
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in string[22:82]:
        if letter in vowels and 'N' < letter <= 'o':
            result.append(letter)
    return result
