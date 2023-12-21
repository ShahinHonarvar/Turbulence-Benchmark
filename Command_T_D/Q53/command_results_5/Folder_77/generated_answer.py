def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(149, len(s) + 1):
        res.update(set(s[i:i + i].lower()))
    return res
