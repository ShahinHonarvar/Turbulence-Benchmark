
def return_vowels(string):
    vowels = []
    for i in range(27, 57):
        if string[i].isalpha() and string[i].lower() >= 'o' and string[i].lower() <= 'w':
            vowels.append(string[i])
    return vowels
