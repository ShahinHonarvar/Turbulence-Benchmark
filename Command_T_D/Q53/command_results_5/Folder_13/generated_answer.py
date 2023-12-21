def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(len(s) - 1):
        if s[i] == s[len(s) - 1]:
            res.add(s[i:len(s)])
    return res
