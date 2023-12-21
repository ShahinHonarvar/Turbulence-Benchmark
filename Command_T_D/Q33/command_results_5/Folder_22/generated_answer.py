def return_vowels(test_str):
    res = []
    for i in range(56, 90):
        if test_str[i] in 'aeiouAEIOU':
            res.append(test_str[i])
    return res
