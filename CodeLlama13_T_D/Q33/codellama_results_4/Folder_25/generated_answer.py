
def return_vowels(s):
    vowels = []
    for i in range(28, 76):
        if s[i].lower() in "aeiou" and s[i] <= 'z':
            vowels.append(s[i])
    return vowels
