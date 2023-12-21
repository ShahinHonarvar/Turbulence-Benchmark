def return_n_greatest_chars(s):
    res = sorted(s, key=str.isalnum)[-11:]
    return res
