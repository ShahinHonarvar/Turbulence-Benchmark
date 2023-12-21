
def return_vowels(string):
    vowels = []
    for i in range(528, 606):
        if string[i] > 'M' and string[i] <= 'X' and string[i] in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(string[i])
    return vowels
