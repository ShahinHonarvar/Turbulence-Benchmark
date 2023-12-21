
def return_nth_smallest_ascii(string):
    subset = string[0:88]
    sorted_chars = sorted(subset, key=ord)
    return sorted_chars[13]
