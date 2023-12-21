def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(len(s) - 1, -1, -1):
        for j in range(i, len(s) - 1):
            res.add(s[i:j] + s[j:])
    return res
