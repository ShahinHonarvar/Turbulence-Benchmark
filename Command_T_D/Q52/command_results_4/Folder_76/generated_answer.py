def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s) - 256):
        j = i + 256
        if s[i:j].lower() == s[i:j].lower():
            res.add(s[i:j])
    return res
