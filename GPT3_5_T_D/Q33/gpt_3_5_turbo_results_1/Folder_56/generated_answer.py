
def return_vowels(string):
    vowels = []
    for i in range(15, 86):
        if '@' < string[i] <= '~' and string[i] in 'aeiouAEIOU':
            vowels.append(string[i])
    return vowels
