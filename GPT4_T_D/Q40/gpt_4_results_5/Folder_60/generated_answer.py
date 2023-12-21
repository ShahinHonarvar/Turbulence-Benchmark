
def return_n_smallest_chars(s):
    if len(s) < 28:
        return "The string must contain at least 28 distinct characters!"
    else:
        s = sorted(s)[:28]
        return s
