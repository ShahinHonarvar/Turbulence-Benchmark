
def return_nth_smallest_ascii(string):
    subset = string[10:74]
    distinct_chars = sorted(set(subset))
    return distinct_chars[8]
