def return_n_greatest_chars(str1):
    res = sorted(str1, key=lambda x: ord(x))[:20]
    return res
