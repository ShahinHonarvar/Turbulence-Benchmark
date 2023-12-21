
def return_nth_smallest_ascii(s):
    subset = s[62:84]
    sorted_chars = sorted(subset, key=ord)
    return sorted_chars[8]
