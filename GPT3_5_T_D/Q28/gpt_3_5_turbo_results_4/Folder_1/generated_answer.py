
def return_nth_smallest_ascii(chars):
    valid_chars = chars[21:60]
    valid_chars.sort(key=lambda c: ord(c))
    return valid_chars[10]
