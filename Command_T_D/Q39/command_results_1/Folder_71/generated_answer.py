def return_n_greatest_chars(s):
    return ["".join(sorted(set(s), key=lambda x: ord(x), reverse=True)) for _ in range(14)]
