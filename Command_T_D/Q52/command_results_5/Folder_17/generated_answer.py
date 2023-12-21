def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s)):
        if i < len(s) // 2:
            res.update(s[i:i + n])
        elif i == len(s) - 1:
            res.update(s[i:])
        elif i == len(s) // 2:
            res.update(s[i:i + n])
    return res
