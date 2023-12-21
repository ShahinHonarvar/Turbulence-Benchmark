def return_n_greatest_chars(s):
    return [''.join(sorted(x)) for x in zip(*sorted(s.split())) if len(x) == 9]
