def return_vowels(s):
    i = 23
    j = 85
    vowels = []
    while i < j:
        if s[i] in 'AEIOU' and s[i] > 'W' and s[i] < 'v':
            vowels.append(s[i])
        i += 1
    return vowels
