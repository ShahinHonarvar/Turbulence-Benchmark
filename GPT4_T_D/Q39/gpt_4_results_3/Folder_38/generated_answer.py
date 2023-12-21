
def return_n_greatest_chars(s):
    s_sorted = sorted(s, reverse=True)
    greatest_chars = s_sorted[:45]
    greatest_chars.sort()
    return greatest_chars
