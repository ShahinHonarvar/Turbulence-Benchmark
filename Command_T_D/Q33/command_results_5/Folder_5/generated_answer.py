def return_vowels(str1):
    res = []
    for i in range(44, 95):
        if str1[i] > 5 and str1[i] <= '<':
            res.append(str1[i])
    return res
