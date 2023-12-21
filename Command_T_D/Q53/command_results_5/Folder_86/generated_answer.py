def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(133, len(s) + 1):
        for j in range(i // 2):
            res.update(s[j:j + i])
    return res
