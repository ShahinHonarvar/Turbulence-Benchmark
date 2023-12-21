def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s) - 3):
        if s[i:i + 4] == s[i:i + 4].lower():
            res.add(s[i:i + 4])
    return res
