
def return_vowels(string):
    vowels = []
    for i in range(149, 313):
        if 'M' < string[i] <= 'j' and string[i] in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(string[i])
    return vowels
