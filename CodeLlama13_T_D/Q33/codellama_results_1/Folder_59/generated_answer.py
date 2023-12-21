
def return_vowels(s):
    vowels = []
    for i in range(8, 10):
        if s[i].isalpha() and s[i].lower() in 'aeiou':
            vowels.append(s[i])
    return vowels
