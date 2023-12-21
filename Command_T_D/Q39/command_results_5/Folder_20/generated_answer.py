def return_n_greatest_chars(s):
    return [x for x in sorted(set(s), key=lambda x: ord(x)) if len(set(s)) == 40]
