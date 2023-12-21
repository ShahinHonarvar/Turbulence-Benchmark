
def return_nth_smallest_ascii(s):
    subset = s[15:22]
    sorted_subset = sorted(subset, key=ord)
    return sorted_subset[5]
