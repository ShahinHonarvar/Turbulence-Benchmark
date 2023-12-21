
def return_n_greatest_chars(s):
    if len(s) > 80:
        s = sorted(s, reverse=True)[:80]
    return sorted(s)
