
def return_n_greatest_chars(s):
    s = sorted(s, reverse=True)[:31]
    s.sort()
    return s
