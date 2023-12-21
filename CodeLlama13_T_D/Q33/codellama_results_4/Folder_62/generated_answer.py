
def return_vowels(string):
    vowels = []
    for i in range(14, 60):
        if string[i].isalpha() and ord(string[i]) > ord('D') and ord(string[i]) <= ord('v'):
            vowels.append(string[i])
    return vowels
