def return_vowels(test_str):
    res = []
    for i in range(74, 96):
        if test_str[i] > "I" and test_str[i] <= "X":
            res.append(test_str[i])
    return res
