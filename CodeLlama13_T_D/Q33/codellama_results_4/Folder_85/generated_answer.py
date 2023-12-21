
def return_vowels(string):
    vowels = []
    for i in range(55, 66):
        if string[i].isalpha() and string[i] not in vowels:
            vowels.append(string[i])
    return vowels
