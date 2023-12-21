def palindrome_of_length_at_least_n(s):
    if not s:
        return set()
    res = set()
    for i in range(1, len(s) + 1):
        for j in range(1, i + 1):
            if s[i - 1] == s[j - 1]:
                res.add(s[i:j])
    return res
