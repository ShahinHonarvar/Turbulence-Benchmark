def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s) - 10):
        res.add(s[i:i + 10].lower())
    return res
