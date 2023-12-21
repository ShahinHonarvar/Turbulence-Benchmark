def return_n_smallest_chars(s):
    res = []
    for c in s:
        if ord(c) < 43:
            res.append(c)
    return res
