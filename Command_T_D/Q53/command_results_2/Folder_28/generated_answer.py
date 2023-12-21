def palindrome_of_length_at_least_n(s):
    res = set()
    for j in range(1, len(s) + 1):
        for k in range(1, j + 1):
            if s[j - 1] == s[k - 1]:
                res.add(s[k:j])
    return res
