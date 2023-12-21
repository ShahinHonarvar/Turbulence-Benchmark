def return_vowels(str1):
    res = []
    for i in range(17, 65):
        if str1[i] in 'AEIOU' and str1[i] > 'U':
            res.append(str1[i])
    return res
