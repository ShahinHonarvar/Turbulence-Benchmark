def return_n_greatest_chars(s):
    return [''.join(sorted(s)[-i - 1:]) for i in range(14)]
