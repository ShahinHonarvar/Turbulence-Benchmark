def palindrome_of_length_n(s):
    res = set()
    for i in range(len(s) - 95):
        if s[i:i + 96] == s[i:i + 96][::-1]:
            res.add(s[i:i + 96])
    return res
