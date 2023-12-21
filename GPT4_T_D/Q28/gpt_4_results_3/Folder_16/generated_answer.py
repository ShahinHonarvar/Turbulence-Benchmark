
def return_nth_smallest_ascii(s):
    substr = s[18:46]
    sorted_chars = sorted(substr, key=ord)
    return sorted_chars[6]
