def palindrome_of_length_n(s):
    res = set()
    for c in range(len(s) - 1, -1, -1):
        for l in range(c + 1, min(len(s) - 1, c + 186)):
            if s[l:c] == s[c:l]:
                res.add(s[l:c])
    return res
