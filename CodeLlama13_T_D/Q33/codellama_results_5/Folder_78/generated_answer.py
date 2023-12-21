
def return_vowels(string):
    vowels = []
    for char in string[46:90]:
        if char >= '@' and char <= '[':
            vowels.append(char)
    return vowels
