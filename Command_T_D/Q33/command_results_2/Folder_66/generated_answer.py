def return_vowels(str1):
    res = []
    for i in range(63, 79):
        if str1[i] in 'AEIOU':
            res.append(str1[i])
    return res
