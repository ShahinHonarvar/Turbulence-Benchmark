def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s) - 35):
        if s[i:i + 37] == s[i:i + 37].lower():
            res.add(s[i:i + 37])
    return res
