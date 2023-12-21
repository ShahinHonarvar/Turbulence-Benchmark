
def return_nth_smallest_ascii(string):
    chars = string[4:34]
    unique_chars = list(set(chars))
    unique_chars.sort()
    return unique_chars[3]
