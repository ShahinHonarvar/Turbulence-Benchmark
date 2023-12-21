def return_n_greatest_chars(s):
    return sorted(s, key=lambda c: c[0], reverse=True)[:2]
