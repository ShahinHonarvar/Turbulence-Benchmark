def return_n_greatest_chars(str):
    res = sorted(str, key=lambda x: ord(x))[:60]
    return res
