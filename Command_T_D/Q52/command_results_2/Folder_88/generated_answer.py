def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s)):
        res.update(s[i:][::-1])
    return res
