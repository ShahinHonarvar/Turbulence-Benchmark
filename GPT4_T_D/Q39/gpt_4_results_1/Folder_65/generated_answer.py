
def return_n_greatest_chars(s):
    s = sorted(s, key=ord, reverse=True)
    return s[:27]
