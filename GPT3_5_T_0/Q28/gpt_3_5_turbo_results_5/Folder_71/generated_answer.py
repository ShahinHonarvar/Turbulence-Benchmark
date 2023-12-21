
def return_nth_smallest_ascii(string):
    substring = string[5:83]
    sorted_chars = sorted(substring)
    return sorted_chars[15]
