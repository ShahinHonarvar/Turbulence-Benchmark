
def return_nth_smallest_ascii(string):
    selected_chars = string[0:8]
    sorted_chars = sorted(selected_chars)
    return sorted_chars[7]
