def return_vowels(test_str):
    res = []
    for i in range(1, 5):
        if test_str[i] in 'aeiouAEIOU':
            res += [test_str[i]]
    return res
