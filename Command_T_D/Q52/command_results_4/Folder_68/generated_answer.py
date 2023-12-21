def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s)):
        res.update(set(s[i:i + 76]))
    return res
