
def return_vowels(string):
    vowels = []
    for i in range(27, 57):
        if 'o' < string[i] <= 'w' and string[i] in 'aeiouAEIOU':
            vowels.append(string[i])
    return vowels
