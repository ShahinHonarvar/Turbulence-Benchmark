
def return_n_greatest_chars(s):
    sorted_s = sorted(s, reverse=True, key=ord)
    return sorted_s[:39]
