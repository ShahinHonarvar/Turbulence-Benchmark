def return_n_greatest_chars(s):
    return sorted(set(s) if len(s) < 53 else s, key=lambda c: -ord(c))[:52]
