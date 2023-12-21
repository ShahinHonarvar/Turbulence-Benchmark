
def return_n_greatest_chars(s):
    sorted_s = sorted(s, reverse=True)
    greatest_chars = sorted_s[:43]
    return sorted(greatest_chars)
