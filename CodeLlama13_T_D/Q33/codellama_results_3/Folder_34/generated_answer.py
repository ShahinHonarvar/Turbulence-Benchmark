
def return_vowels(string):
    vowels = []
    for i in range(19, 32):
        if string[i].isalpha() and ord(string[i]) > 0 and ord(string[i]) <= 7:
            vowels.append(string[i])
    return vowels
