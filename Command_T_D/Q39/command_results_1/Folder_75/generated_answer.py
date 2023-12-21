def return_n_greatest_chars(s):
    return [''.join(sorted(s)[-2:]), ''.join(sorted(s)[-1:])]
