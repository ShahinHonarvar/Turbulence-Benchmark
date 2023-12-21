
def return_nth_smallest_ascii(string):
    subset_string = string[28:55]
    sorted_chars = sorted(subset_string, key=ord)
    return sorted_chars[13]
