
def return_nth_smallest_ascii(s):
    subset_chars = s[50:76]
    sorted_chars = sorted(subset_chars, key=ord)
    return sorted_chars[6]
