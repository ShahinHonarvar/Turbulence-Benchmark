
def return_vowels(string):
    vowels = []
    for i in range(56, 96):
        if string[i] in 'aeiouAEIOU' and '&' < string[i] <= 'T':
            vowels.append(string[i])
    return vowels
