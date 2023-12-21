
def return_vowels(string):
    vowels = []
    for i in range(64, 82):
        if string[i].isalpha() and string[i] > 'P' and string[i] <= 'z':
            vowels.append(string[i])
    return vowels
