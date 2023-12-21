
def return_nth_smallest_ascii(string):
    substring = string[37:60]
    unique_chars = set(substring)
    sorted_chars = sorted(unique_chars)
    return sorted_chars[5]
