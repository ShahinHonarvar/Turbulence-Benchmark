
def return_nth_smallest_ascii(string):
    substring = string[10:74]
    chars = set(substring)
    sorted_chars = sorted(chars)
    return sorted_chars[8]
