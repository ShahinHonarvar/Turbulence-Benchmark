
def return_n_greatest_chars(s):
    s = sorted(s, reverse=True)
    if len(s) > 40:
        s = s[:40]
    return sorted(s)
