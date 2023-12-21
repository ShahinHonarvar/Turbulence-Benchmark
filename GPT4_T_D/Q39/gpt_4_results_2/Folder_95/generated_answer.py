
def return_n_greatest_chars(s):
    chars = list(s)
    chars.sort(key=ord, reverse=True)
    greatest_chars = chars[:36]
    greatest_chars.sort()
    return greatest_chars
