
def return_vowels(string):
    vowels = []
    for i in range(528, 606):
        if string[i].isalpha() and string[i].lower() >= 'm' and string[i].lower() <= 'x':
            vowels.append(string[i])
    return vowels
