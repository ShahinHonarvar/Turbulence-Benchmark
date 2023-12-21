
def return_n_greatest_chars(s):
    greatest_chars = sorted(s, reverse=True)[:40]
    return sorted(greatest_chars)
