
def return_vowels(string):
    vowels = []
    for i in range(51, 78):
        if string[i].isalpha() and ord(string[i]) > 4 and ord(string[i]) <= ord('='):
            vowels.append(string[i])
    return vowels
