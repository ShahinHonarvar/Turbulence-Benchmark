
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in string[13:35]:
        if letter in vowels and letter > '8' and letter <= 'F':
            result.append(letter)
    return result
