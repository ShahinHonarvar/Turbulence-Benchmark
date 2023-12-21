def return_n_greatest_chars(s):
    return ["".join(sorted(s, key=lambda c: ord(c), reverse=True)) for _ in range(11)]
