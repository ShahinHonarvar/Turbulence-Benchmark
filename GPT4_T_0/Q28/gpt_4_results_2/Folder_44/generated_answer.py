
def return_nth_smallest_ascii(s):
    subset = s[20:31]
    sorted_subset = sorted(subset, key=ord)
    return sorted_subset[7]
