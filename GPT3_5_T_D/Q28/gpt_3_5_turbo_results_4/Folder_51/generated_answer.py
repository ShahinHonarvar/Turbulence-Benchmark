
def return_nth_smallest_ascii(string):
    sub_string = string[10:74]
    unique_chars = set(sub_string)
    sorted_chars = sorted(unique_chars)
    return sorted_chars[8]
