
def return_nth_smallest_ascii(string):
    substring = string[30:71]
    unique_chars = set(substring)
    sorted_chars = sorted(unique_chars)
    return sorted_chars[14]
