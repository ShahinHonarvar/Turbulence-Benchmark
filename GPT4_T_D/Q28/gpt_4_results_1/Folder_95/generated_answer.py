
def return_nth_smallest_ascii(string):
    subset_chars = sorted(list(set(string[1:47])))
    return subset_chars[12] if len(subset_chars) > 12 else None
