
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in string[1:9]:
        if letter in vowels and '?' < letter <= 'k':
            result.append(letter)
    return result
