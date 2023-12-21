
def return_vowels(string):
    vowels = []
    for i in range(70, 76):
        if string[i].isalpha() and ord(string[i]) > 2 and ord(string[i]) <= ord(':'):
            vowels.append(string[i])
    return vowels
