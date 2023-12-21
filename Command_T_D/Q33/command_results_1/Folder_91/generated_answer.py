def return_vowels(str1):
    res = []
    for i in range(len(str1) - 3):
        if str1[i + 4] in "AEIOU" and str1[i + 8] == 'r':
            res += [str1[i + 4]]
    return res
