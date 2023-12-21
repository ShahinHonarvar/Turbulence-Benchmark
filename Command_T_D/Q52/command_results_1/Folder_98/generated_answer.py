def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s) - 5, -1, -1):
        for j in range(i, i + 6):
            res.add(s[j:j+6])
    return res
