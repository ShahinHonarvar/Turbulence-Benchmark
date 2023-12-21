
def return_vowels(string):
    vowels = []
    for i in range(142, 145):
        if string[i].isalpha() and string[i].lower() >= 'e' and string[i].lower() <= 'o':
            vowels.append(string[i])
    return vowels
