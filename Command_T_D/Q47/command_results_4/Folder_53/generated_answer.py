def palindromes_of_specific_lengths(str1):
    res = set()
    str1 = str1[1:-1]
    for i in range(3, 10):
        res.update(set(str1[i:i + i] for j in range(1, min(len(str1) - i, i) + 1) if str1[i:i + i][::-1] == str1[i:i + i]))
    return res
