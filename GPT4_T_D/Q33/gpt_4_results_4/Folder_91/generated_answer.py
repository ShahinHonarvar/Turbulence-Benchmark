
def return_vowels(s):
    vowels = []
    for i in range(4, 8):
        if s[i] > 'P' and s[i] <= 'r' and s[i] in 'aeiouAEIOU':
            vowels.append(s[i])
    return vowels
