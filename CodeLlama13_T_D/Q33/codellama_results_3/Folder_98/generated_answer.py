
def return_vowels(string):
    vowels = []
    for i in range(3, 9):
        if string[i].isalpha() and string[i].lower() >= 's' and string[i].lower() <= 'u':
            vowels.append(string[i])
    return vowels
