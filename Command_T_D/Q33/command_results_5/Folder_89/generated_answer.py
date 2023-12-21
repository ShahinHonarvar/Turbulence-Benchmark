def return_vowels(s):
    vowels = []
    if s[50] > "i" or s[51] < "v":
        return vowels
    for i in range(50, 51):
        if s[i] in "aeiouAEIOU":
            vowels.append(s[i])
    return vowels
