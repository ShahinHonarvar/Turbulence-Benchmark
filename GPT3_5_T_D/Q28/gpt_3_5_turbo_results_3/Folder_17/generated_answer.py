
def return_nth_smallest_ascii(string):
    substring = string[3:34]
    unique_chars = sorted(set(substring))
    return unique_chars[3]
