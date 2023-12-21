def return_n_greatest_chars(s):
    return [x for x in sorted(s, key=lambda x: x.lower()) if len(set(x)) == 1]
