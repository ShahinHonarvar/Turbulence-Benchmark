
def return_nth_smallest_ascii(s):
    chars = s[0:9]
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[8]
