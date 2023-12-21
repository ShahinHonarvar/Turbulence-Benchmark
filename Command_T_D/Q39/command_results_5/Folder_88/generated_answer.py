def return_n_greatest_chars(s):
    res = sorted(set(s), key=lambda c: c.encode('ascii'))[:84]
    return res
