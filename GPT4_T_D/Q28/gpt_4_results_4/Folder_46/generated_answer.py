
def return_nth_smallest_ascii(s):
    sliced_str = s[34:86]
    sorted_subset = sorted(sliced_str, key=ord)
    return sorted_subset[19]
