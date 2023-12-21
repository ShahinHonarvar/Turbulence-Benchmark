def palindromes_of_specific_lengths(str1):
    str1 = str1[10:74]
    str1 = str1.lower()
    res = set()
    for i in range(6, 8):
        for j in range(len(str1) - i):
            res.add(str1[j:j + i])
    return res
