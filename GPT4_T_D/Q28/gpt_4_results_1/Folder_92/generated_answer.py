
def return_nth_smallest_ascii(chars):
    trimmed_chars = chars[0:4]
    sorted_chars = sorted(trimmed_chars)
    return sorted_chars[3]
