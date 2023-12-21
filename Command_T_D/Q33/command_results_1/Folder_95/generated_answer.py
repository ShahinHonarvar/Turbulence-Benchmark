def return_vowels(s):
    vowels = []
    for i in range(len(s)):
        if i == 32:
            continue
        elif s[i] >= 'a' and s[i] <= 'z':
            vowels.append(s[i])
        elif s[i] >= 'A' and s[i] <= 'Z':
            vowels.append(s[i])
    return vowels
