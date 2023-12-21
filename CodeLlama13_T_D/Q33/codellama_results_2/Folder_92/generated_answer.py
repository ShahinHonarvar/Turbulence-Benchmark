
def return_vowels(string):
    vowels = []
    for i in range(3, 8):
        if string[i].isalpha() and string[i] >= 'E' and string[i] <= 'D':
            vowels.append(string[i])
    return vowels
