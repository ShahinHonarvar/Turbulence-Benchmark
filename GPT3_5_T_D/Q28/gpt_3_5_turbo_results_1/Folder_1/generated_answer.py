
def return_nth_smallest_ascii(string):
    substring = string[21:60]
    unique_chars = sorted(set(substring))
    return unique_chars[10]
