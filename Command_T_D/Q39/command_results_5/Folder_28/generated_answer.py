def return_n_greatest_chars(s):
    return ["".join(sorted(s, key=lambda x: x)) for _ in range(3)]
