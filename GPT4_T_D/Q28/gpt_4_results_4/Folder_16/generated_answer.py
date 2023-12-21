
def return_nth_smallest_ascii(string):
    string_slice = string[18:46]
    sorted_chars = sorted(string_slice, key=ord)
    return sorted_chars[6]
