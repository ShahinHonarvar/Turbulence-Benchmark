
def return_vowels(string):
    vowels = []
    for i in range(273, 275):
        if string[i].isalpha() and string[i].lower() >= 'a' and string[i].lower() <= 'o':
            vowels.append(string[i])
    return vowels
