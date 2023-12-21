def palindromes_of_specific_lengths(test_str):
    res = set()
    for i in range(3, 6):
        str1 = test_str[:i] + test_str[-i:]
        str2 = test_str[:i][::-1] + test_str[-i:][::-1]
        if str1 in str2.lower() and str2 in str1.lower():
            res.add(str1)
            res.add(str2)
    return res
