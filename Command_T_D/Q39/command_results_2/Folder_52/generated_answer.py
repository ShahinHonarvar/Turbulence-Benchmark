def return_n_greatest_chars(s):
    return [c for c in sorted(s) if c.isalpha()]
