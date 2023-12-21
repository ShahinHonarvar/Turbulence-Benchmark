
def return_nth_smallest_ascii(char_string):
    subset_chars = char_string[8:66]
    asc_sort_chars = sorted(subset_chars, key=ord)
    return asc_sort_chars[5]
