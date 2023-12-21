
def return_n_smallest_chars(s):
    s = sorted(s)
    s = s[:61]
    return sorted(s, reverse=True)
