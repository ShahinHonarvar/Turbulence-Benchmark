
def return_vowels(string):
    vowels = []
    for i in range(171, 402):
        char = string[i]
        if char >= 'I' and char <= 'k':
            vowels.append(char)
    return vowels
