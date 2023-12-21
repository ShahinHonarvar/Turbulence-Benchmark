def palindrome_of_length_at_least_n(s):
    res = set()
    for i in range(len(s) - 1, -1, -1):
        res |= set(s[i:][::-1])
    return res
