def return_n_greatest_chars(s):
    return list(sorted(set(s), key=lambda c: ord(c), reverse=True))[:46]
