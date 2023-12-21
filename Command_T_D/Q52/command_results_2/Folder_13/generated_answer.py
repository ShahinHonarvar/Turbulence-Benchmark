def palindrome_of_length_n(s):
    res = set()
    for c in s.lower():
        res.update(set(c[i:i+2] for i in range(len(c) - 1)))
    return res
