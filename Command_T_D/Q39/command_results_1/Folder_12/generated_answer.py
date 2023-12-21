def return_n_greatest_chars(s):
    return [c for c in sorted(set(s), key=lambda x: ord(x)) if len(list(filter(lambda x: ord(x) == ord(c), s))) == 1]
