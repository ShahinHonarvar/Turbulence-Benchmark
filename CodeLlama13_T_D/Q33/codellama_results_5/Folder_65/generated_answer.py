
def return_vowels(string):
    vowels = []
    for i in range(71, 88):
        char = string[i]
        if 'a' <= char <= 'p':
            vowels.append(char)
    return vowels
