
def return_vowels(string):
    vowels = []
    for i in range(34, 58):
        if string[i].isalpha() and string[i] > 'b' and string[i] <= 'o':
            vowels.append(string[i])
    return vowels
