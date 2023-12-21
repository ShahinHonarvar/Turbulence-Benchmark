def return_vowels(s):
    return [i for i in range(23, 57) if i not in s or s[i] > '0' and s[i] <= 'd']
