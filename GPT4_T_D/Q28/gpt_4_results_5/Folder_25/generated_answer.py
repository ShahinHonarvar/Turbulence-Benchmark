
def return_nth_smallest_ascii(s):
    segment = s[34:69]
    sorted_chars = sorted(segment, key=ord)
    return sorted_chars[5]
