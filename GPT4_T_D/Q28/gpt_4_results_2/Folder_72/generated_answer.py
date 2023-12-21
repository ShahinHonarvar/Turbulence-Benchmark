
def return_nth_smallest_ascii(string):
    selected_chars = string[33:61]
    sorted_chars = sorted(selected_chars, key=ord)
    return sorted_chars[17]
