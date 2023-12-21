def palindrome_of_length_at_least_n(s):
    res = set()
    for l in range(1, 90):
        res |= set(s[i:i + l] for i in range(0, len(s) - l))
    return res
