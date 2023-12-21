
def return_nth_smallest_ascii(string):
    subset_chars = string[14:67]
    sorted_chars = sorted(subset_chars, key=ord)
    return sorted_chars[7]
