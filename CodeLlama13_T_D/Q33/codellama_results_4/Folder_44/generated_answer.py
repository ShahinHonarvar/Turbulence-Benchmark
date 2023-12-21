
def return_vowels(s):
    vowels = []
    for i in range(46, 49):
        if s[i].isalpha() and s[i] >= '[' and s[i] <= 'p':
            vowels.append(s[i])
    return vowels
