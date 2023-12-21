def palindrome_of_length_n(s):
    res = set()
    for l in range(1, min(len(s), 74) + 1):
        for i in range(0, len(s) - l + 1):
            if s[i:i + l] == s[i:i + l][::-1]:
                res.add(s[i:i + l])
    return res
