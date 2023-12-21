
def return_nth_smallest_ascii(s):
    subset = s[20:31]
    sorted_chars = sorted(subset, key=ord)
    return sorted_chars[7]
