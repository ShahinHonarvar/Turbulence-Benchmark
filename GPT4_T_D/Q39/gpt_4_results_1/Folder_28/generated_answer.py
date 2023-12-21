
def return_n_greatest_chars(s):
    s = sorted(s, reverse=True)[0:3]
    s.sort()
    return s
