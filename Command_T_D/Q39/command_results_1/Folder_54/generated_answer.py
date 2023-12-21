def return_n_greatest_chars(s):
    return sorted(set(s), key=lambda c: c.lower(), reverse=True)[:79]
