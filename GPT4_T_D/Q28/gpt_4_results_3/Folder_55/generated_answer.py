
def return_nth_smallest_ascii(s):
    subset = s[:13]
    sorted_chars = sorted(list(subset))
    return sorted_chars[12]
