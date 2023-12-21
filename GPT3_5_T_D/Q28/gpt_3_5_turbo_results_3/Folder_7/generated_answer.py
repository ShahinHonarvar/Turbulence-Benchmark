
def return_nth_smallest_ascii(string):
    substring = string[12:56]
    unique_chars = list(set(substring))
    unique_chars.sort()
    return unique_chars[16]
