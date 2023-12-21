
def return_n_greatest_chars(s):
    sorted_s = sorted(s, reverse=True)
    greatest_chars = sorted_s[:72]
    greatest_chars.sort()
    return greatest_chars
