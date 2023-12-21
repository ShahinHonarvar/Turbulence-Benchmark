def palindrome_of_length_at_least_n(s):
    res = set()
    for c in s:
        for i in range(1, 64):
            if c in s[i:]:
                res.add(s[i:i + i])
    return res
