
def return_vowels(string):
    vowels = []
    for i in range(47, 61):
        if string[i].isalpha() and ord(string[i]) > 9 and ord(string[i]) <= ord('O'):
            vowels.append(string[i])
    return vowels
