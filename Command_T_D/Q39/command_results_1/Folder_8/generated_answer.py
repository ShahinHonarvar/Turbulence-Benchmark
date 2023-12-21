def return_n_greatest_chars(s):
    return sorted(s, key=lambda x: ord(x), reverse=True)[:83]
