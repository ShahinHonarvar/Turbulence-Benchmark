def return_n_greatest_chars(s):
    res = sorted(set(s))[:85]
    res.sort(reverse=True)
    return res
