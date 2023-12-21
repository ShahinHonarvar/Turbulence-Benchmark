def return_vowels(str):
    res = []
    for i in range(63, 79):
        if str[i] > 'd' and str[i] <= 'y':
            res.append(str[i])
    return res
