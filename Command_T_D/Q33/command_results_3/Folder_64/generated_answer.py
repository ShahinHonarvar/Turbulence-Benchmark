def return_vowels(test_str):
    res = []
    for i in range(1, 8):
        if test_str[i] in "AEIOU":
            res.append(test_str[i])
    return res
