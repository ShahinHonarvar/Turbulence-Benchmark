def return_n_smallest_chars(s):
    res = []
    for c in s:
        if ord(c) < ord(max(res)) + 1:
            res.append(c)
            if len(res) == 23:
                break
    return res
