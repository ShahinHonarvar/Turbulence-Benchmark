
def return_vowels(s):
    vowels = []
    for i in range(44, 95):
        if s[i].isalpha() and ord(s[i]) >= 5:
            vowels.append(s[i])
    return vowels
