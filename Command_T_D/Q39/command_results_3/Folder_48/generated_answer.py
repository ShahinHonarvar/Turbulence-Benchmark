def return_n_greatest_chars(str):
    res = list(sorted(set(str), key=lambda x: ord(x), reverse=True)[:12])
    return res
