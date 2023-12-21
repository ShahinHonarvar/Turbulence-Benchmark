
def return_nth_smallest_ascii(characters):
    subset = list(characters[:16])
    subset.sort(key=ord)
    return subset[15]
