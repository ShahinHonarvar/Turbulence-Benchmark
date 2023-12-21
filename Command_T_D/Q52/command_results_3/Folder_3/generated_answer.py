def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s) - 1, -1, -1):
        if s[i] == s[len(s) - 1 - i]:
            res.add(s[i:len(s) - 1 - i])
    return res
