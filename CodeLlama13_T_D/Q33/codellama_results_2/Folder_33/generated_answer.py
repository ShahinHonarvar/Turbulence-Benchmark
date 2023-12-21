
def return_vowels(string):
    vowels = []
    for i in range(163, 771):
        char = string[i]
        if char >= ':' and char <= 'E' and char in 'aeiouAEIOU':
            vowels.append(char)
    return vowels
