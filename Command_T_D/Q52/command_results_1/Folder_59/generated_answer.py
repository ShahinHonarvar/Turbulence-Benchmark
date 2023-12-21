def palindrome_of_length_n(s):
    res = set()
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            res.add(s[i:j])
    return res
