
def return_n_smallest_chars(s):
    if len(s) < 44:
        return "Error: The string must have at least 44 different characters."
    else:
        s_sorted = sorted(s, key=ord)
        s_ascii = s_sorted[:44]
        s_ascii.sort(reverse=True)
        return s_ascii
