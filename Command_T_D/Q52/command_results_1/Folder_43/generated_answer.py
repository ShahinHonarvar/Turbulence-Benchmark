def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s) - 50):
        if s[i:i + 51] == s[i:i + 51].lower():
            res.add(s[i:i + 51])
    return res
