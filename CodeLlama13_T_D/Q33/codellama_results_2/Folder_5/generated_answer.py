
def return_vowels(s):
    vowels = []
    for i in range(44, 95):
        if s[i].isalpha() and s[i].lower() in "aeiou" and ord(s[i]) <= 230:
            vowels.append(s[i])
    return vowels
