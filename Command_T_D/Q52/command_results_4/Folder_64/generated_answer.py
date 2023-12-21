def palindrome_of_length_n(s):
    if not s:
        return set()
    res = set()
    for i in range(len(s) - 8):
        res.add(s[i:i + 9])
    return res
