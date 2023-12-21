def return_n_greatest_chars(s):
    s = sorted(s, key=lambda c: ord(c))[:47]
    return s
