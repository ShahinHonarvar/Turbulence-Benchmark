
def return_vowels(string):
    vowels = []
    for i in range(32, 61):
        if string[i].isalpha() and string[i] >= '?' and string[i] <= 'P':
            vowels.append(string[i])
    return vowels
