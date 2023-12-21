
def return_n_greatest_chars(s):
    if len(s) > 38:
        s = sorted(set(s), key=ord, reverse=True)[:38]
    elif len(s) < 38:
        s = sorted(set(s), key=ord, reverse=True)
    return s
