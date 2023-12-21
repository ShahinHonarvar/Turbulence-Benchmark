
def return_vowels(string):
    vowels = []
    for i in range(86, 99):
        char = string[i]
        if char >= 'E' and char <= 'r':
            vowels.append(char)
    return vowels
