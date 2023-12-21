def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s) - 1):
        for j in range(i, len(s) - 1):
            res.add(s[i:j + 1])
    return res
