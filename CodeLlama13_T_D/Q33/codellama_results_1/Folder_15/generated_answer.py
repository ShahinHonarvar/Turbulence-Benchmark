
def return_vowels(s):
    vowels = []
    for i in range(5, 7):
        if s[i].isalpha() and ord(s[i]) > 3 and ord(s[i]) <= ord('^'):
            vowels.append(s[i])
    return vowels
