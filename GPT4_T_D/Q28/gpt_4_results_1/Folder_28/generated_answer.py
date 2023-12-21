
def return_nth_smallest_ascii(s):
    subset = list(s[25:78])
    subset.sort(key=ord)
    return subset[15]
