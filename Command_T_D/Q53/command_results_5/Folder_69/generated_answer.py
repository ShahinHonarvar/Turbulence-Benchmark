def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(len(s)):
        if i < len(s) - i:
            res.add(s[i:i + i])
    return res
