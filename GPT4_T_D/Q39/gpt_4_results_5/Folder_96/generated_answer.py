
def return_n_greatest_chars(s):
    s = sorted(s, reverse=True)
    if len(s) >= 20:
        return s[:20]
    else:
        return s
