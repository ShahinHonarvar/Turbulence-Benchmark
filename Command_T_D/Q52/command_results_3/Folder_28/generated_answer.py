def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s) - 43):
        if s[i:i + 43] == s[i + 42:i + 43]:
            res.add(s[i:i + 43])
    return res
