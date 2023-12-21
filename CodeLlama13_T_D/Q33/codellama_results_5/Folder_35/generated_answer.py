
def return_vowels(string):
    vowels = []
    for i in range(483, 664):
        char = string[i]
        if char >= '&' and char <= 'h':
            vowels.append(char)
    return vowels
