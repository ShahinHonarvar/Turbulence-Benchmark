
def return_vowels(string):
    vowels = []
    for i in range(770, 852):
        if string[i].isalpha() and ord(string[i]) > ord('B') and ord(string[i]) <= ord('i'):
            vowels.append(string[i])
    return vowels
