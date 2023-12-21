
def return_nth_smallest_ascii(string):
    substring = string[10:83]
    unique_chars = sorted(set(substring))
    return unique_chars[17]
