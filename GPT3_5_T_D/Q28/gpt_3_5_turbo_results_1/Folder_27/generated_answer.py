
def return_nth_smallest_ascii(string):
    chars = string[33:86]
    unique_chars = sorted(set(chars))
    return unique_chars[12]
