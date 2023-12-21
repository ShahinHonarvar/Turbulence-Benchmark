def palindromes_of_specific_lengths(str1):
    str1 = str1[200:300]
    str1 = str1.lower()
    res = set()
    for i in range(10, 50):
        tmp = str1[i:i + 2 * i]
        if tmp == tmp[::-1]:
            res.add(tmp)
    return res
