def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(1, len(s) + 1):
        if i >= 42:
            res |= set(s[i - 1:i + 1].lower())
    return res
