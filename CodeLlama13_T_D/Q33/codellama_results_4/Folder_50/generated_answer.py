
def return_vowels(string):
    vowels = []
    for i in range(10, 54):
        if string[i].isalpha() and string[i].lower() >= 'a' and string[i].lower() <= 'w':
            vowels.append(string[i])
    return vowels
