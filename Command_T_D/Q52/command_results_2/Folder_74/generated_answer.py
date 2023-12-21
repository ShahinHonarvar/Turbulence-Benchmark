def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s)):
        for j in range(len(s) - 1, i, -1):
            if s[i] == s[j]:
                res.add(s[i:j + 1])
    return res
