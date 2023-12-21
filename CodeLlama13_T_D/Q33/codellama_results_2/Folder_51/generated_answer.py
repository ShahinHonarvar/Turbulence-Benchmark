
def return_vowels(string):
    vowels = []
    for i in range(56, 68):
        if string[i].isalpha() and string[i].upper() >= 'M' and string[i].upper() <= 'X':
            vowels.append(string[i])
    return vowels
