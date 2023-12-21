def return_n_smallest_chars(s):
    res = []
    for c in s:
        if ord(c) < ord('z'):
            res.append(c)
            if len(res) == 76:
                break
    return res
