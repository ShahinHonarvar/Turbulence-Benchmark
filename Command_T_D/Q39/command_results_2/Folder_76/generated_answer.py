def return_n_greatest_chars(s):
    return [x for x in sorted(s)[::-1][:3]]
