
def return_n_greatest_chars(s):
    s = sorted(s, reverse=True)
    greatest_chars = s[:82]
    greatest_chars.sort()
    return greatest_chars
