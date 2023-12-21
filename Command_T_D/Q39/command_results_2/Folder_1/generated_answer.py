def return_n_greatest_chars(s):
    return sorted(s, key=lambda x: (ord(x), -x))[:11]
