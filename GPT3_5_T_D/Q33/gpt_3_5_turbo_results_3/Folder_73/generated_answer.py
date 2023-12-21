
def return_vowels(string):
    vowels = []
    for i in range(47, 89):
        if '@' < string[i] <= 'n' and string[i] in 'aeiouAEIOU':
            vowels.append(string[i])
    return vowels
