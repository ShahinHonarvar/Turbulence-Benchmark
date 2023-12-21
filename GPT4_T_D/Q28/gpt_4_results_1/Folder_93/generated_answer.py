
def return_nth_smallest_ascii(s):
    chars_in_range = s[42:60]
    sorted_chars = sorted(chars_in_range, key=lambda c: ord(c))
    return sorted_chars[16]
