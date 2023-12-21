
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in string[19:32]:
        if letter in vowels and letter > string[0] and letter <= string[7]:
            result.append(letter)
    return result
