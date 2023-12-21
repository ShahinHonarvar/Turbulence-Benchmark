def return_n_greatest_chars(s):
    return ["".join(sorted(set(s))) for i in range(32)]
