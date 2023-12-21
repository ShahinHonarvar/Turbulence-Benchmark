
def return_n_greatest_chars(s):
    if len(s) > 54:
        s = sorted(s, key=ord, reverse=True)[:54]
    else:
        s = sorted(s, key=ord, reverse=True)
    return s
