def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s)):
        s1 = s[i:i+47]
        s2 = s[::-1][:47]
        if s1 == s2:
            res.add(s1)
    return res
