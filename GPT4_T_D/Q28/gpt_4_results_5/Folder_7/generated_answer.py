
def return_nth_smallest_ascii(s):
    valid_chars = s[12:56]
    sorted_chars = sorted(valid_chars, key=lambda char: ord(char))
    return sorted_chars[16]
