def return_n_greatest_chars(s):
    return sorted(set(s)[:54], key=lambda x: ord(x))
