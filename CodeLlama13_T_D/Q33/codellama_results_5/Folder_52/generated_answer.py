
def return_vowels(string):
    vowels = []
    for i in range(24, 68):
        if string[i].isalpha() and ord(string[i]) > ord('f') and ord(string[i]) <= ord('|'):
            vowels.append(string[i])
    return vowels
