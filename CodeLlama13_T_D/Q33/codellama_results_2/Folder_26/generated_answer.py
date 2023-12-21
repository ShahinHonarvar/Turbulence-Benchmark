
def return_vowels(string):
    vowels = []
    for i in range(10, 82):
        if string[i].isalpha() and string[i] >= '$' and string[i] <= '@':
            vowels.append(string[i])
    return vowels
