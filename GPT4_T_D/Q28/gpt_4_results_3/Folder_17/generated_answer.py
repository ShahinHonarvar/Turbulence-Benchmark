
def return_nth_smallest_ascii(str):
    str_subset = str[4:34]
    sorted_chars = sorted(str_subset, key=ord)
    return sorted_chars[3]
