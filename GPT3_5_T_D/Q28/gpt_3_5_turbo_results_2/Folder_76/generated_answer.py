
def return_nth_smallest_ascii(string):
    substring = string[18:67]
    unique_chars = sorted(set(substring))
    smallest_ascii_char = unique_chars[18]
    return smallest_ascii_char
