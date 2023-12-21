
def return_nth_smallest_ascii(s):
    subset = s[10:83]
    ordered_ascii = sorted(set(subset), key=ord)
    return ordered_ascii[17]
