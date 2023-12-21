
def return_vowels(string):
    vowels = []
    for i in range(22, 82):
        if string[i].isalpha() and string[i] > 'N' and string[i] <= 'o':
            vowels.append(string[i])
    return vowels
