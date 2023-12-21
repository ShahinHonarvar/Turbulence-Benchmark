def return_n_greatest_chars(s):
    return sorted(set(s), key=lambda c: c.encode("ascii"), reverse=True)[:36]
