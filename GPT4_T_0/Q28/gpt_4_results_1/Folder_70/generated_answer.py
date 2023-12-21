
def return_nth_smallest_ascii(s):
    subset = s[28:55]
    sorted_chars = sorted(subset, key=ord)
    return sorted_chars[13]
