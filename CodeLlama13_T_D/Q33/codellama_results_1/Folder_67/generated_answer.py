
def return_vowels(string):
    vowels = []
    for i in range(21, 59):
        if string[i].isalpha() and string[i].lower() >= 'a' and string[i].lower() <= 'z':
            vowels.append(string[i])
    return vowels
