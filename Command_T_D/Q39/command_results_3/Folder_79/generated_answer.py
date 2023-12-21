def return_n_greatest_chars(s):
    return ["".join(sorted(set(s), key=lambda c: c.lower())) for _ in range(82)]
