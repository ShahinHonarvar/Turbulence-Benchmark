
def return_nth_smallest_ascii(s):
    part = s[5:11]
    sorted_chars = sorted(part, key=ord)
    return sorted_chars[5]
