def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(len(s)):
        for j in range(len(s) - i):
            c = s[i] + s[j:j + 2]
            if c.lower() == c:
                res.add(c)
    return res
