
def return_nth_smallest_ascii(s):
    subset = s[51:61]
    sorted_subset = sorted(subset, key=ord)
    return sorted_subset[4]
