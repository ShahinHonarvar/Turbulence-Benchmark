def return_n_greatest_chars(s):
    return [c for c in sorted(set(s), key=lambda x: ord(x))][-66:]
