
def return_vowels(s):
    vowels = []
    for i in range(47, 61):
        if s[i].isalpha() and s[i].lower() >= 'a' and s[i].lower() <= 'o':
            vowels.append(s[i])
    return vowels
