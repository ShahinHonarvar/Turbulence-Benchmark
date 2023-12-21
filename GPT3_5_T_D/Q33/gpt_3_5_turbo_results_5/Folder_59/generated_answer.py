
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in string[8:9]:
        if letter.lower() in vowels and 'Y' < letter.lower() <= 's':
            result.append(letter)
    return result
