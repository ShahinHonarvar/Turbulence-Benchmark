def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s) - 1, -1, -1):
        if s[i] in s[i][::-1]:
            res.add(s[i][::-1])
    return res
