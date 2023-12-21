
def return_vowels(s):
    vowels = []
    for i in range(202, 872):
        if s[i] > '3' and s[i] <= '>':
            vowels.append(s[i])
    return vowels
