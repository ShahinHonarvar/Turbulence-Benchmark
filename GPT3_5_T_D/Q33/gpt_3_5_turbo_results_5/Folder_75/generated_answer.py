
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for letter in string[20:41]:
        if 'K' < letter <= 'Z' and letter.lower() in vowels:
            result.append(letter)
    return result
