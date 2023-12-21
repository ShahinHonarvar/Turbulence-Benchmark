def return_n_smallest_chars(s):
    res = []
    for c in s:
        res.append(c)
        res = res[:21]
        break
    return res
