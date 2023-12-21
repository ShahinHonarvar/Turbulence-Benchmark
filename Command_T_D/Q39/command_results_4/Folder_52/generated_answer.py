def return_n_greatest_chars(s):
    return [''.join(sorted(s, key=lambda c: c.lower()))]
