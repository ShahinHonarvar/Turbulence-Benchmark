
def return_n_greatest_chars(s):
    s = sorted(s, reverse=True)[:40]
    s.sort()
    return s
