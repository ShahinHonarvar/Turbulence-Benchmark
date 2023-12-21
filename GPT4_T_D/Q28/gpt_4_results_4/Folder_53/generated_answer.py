
def return_nth_smallest_ascii(s):
    subset_s = s[40:61]
    sorted_chars = sorted(subset_s, key=ord)
    return sorted_chars[18]
