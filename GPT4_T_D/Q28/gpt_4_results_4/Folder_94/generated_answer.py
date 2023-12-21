
def return_nth_smallest_ascii(s):
    subset = s[6:59]
    sorted_chars = sorted(subset, key=ord)
    return sorted_chars[18]
