
def return_vowels(string):
    vowels = []
    for i in range(22, 82):
        if string[i].isalpha() and string[i].lower() >= 'n' and string[i].lower() <= 'o':
            vowels.append(string[i])
    return vowels
