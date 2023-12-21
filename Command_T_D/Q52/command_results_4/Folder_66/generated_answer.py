def palindrome_of_length_n(s):
    res = set()
    for i in range(25):
        res.update(set(s[i:i+2].lower()))
    return res
