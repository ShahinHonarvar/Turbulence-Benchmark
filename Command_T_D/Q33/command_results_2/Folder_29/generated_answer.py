def return_vowels(test_str):
    res = []
    for index in range(19, 20):
        if test_str[index] > "<" and test_str[index] <= "p":
            res.append(test_str[index])
    return res
