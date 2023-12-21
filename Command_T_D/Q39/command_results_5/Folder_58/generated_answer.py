def return_n_greatest_chars(s):
    return [char for char in sorted(set(s), key=lambda c: ord(c), reverse=True) if len(set(s)) == 49]
