
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []

    for letter in string[17:65]:
        if 'U' < letter <= '{' and letter.lower() in vowels:
            result.append(letter)

    return result
