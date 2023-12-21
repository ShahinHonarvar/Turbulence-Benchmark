def palindrome_of_length_at_least_n(s):
    res = set()
    for c in range(63, -1, -1):
        for i in range(len(s) - c + 1):
            j = i + c
            if s[i:j] == s[j:i]:
                res.add(s[i:j])
    return res
