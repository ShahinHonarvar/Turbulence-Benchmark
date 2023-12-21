
def return_nth_smallest_ascii(s):
    substr = s[60:89]
    sorted_chars = sorted([ch for ch in substr], key=ord)
    return sorted_chars[6]
