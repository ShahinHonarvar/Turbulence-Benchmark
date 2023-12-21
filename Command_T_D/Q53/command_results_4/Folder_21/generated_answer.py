def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(len(s)):
        for j in range(i, len(s), 2):
            res.add(s[i:j])
    return res
