
def return_n_greatest_chars(s):
    s = sorted(s, reverse=True)
    greatest_chars = s[:68]
    greatest_chars.sort()
    return greatest_chars
