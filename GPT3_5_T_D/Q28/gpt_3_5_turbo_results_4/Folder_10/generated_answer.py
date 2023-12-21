
def return_nth_smallest_ascii(string):
    substring = string[38:83]
    unique_chars = list(set(substring))
    sorted_chars = sorted(unique_chars)
    return sorted_chars[19]
