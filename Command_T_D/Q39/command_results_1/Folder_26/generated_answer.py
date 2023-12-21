def return_n_greatest_chars(s):
    return sorted(s, key=str.lower)[-43:]
