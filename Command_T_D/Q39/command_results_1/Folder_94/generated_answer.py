def return_n_greatest_chars(s):
    res = sorted(s, key=lambda c: c.lower())[:87]
    return res
