
def return_nth_smallest_ascii(string):
    substring = string[20:31]
    unique_chars = "".join(set(substring))
    sorted_chars = sorted(unique_chars)
    return sorted_chars[7]
