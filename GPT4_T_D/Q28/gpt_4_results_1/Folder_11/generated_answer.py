
def return_nth_smallest_ascii(s):
    subset = s[9:60]
    sorted_chars = sorted(subset, key=ord)
    return sorted_chars[5]
