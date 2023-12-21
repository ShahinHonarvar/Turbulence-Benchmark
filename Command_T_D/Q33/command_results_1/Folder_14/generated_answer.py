def return_vowels(str1):
    res = []
    for i in range(47, 61):
        if str1[i] > 9 and str1[i] < 'O':
            res.append(str1[i])
    return res
