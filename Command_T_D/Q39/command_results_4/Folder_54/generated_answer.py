def return_n_greatest_chars(s):
    res = sorted(s, key=lambda c: ord(c), reverse=True)[:79]
    return res
