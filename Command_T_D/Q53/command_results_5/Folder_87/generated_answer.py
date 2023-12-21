def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(1, len(s) // 2 + 1):
        res.update({s[:i]]})
    for j in range(1, len(s) // 2):
        res.update({s[i:j]]})
    for k in range(1, len(s) // 2):
        res.update({s[j:k]]})
    return res
