def return_n_greatest_chars(s):
    return ["".join(sorted(set(s), key=lambda c: ord(c), reverse=True)[:19])]
