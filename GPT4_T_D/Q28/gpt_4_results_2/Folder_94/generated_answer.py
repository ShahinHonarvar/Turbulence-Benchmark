
def return_nth_smallest_ascii(my_string):
    selected_chars = list(my_string[6:59])
    sorted_chars = sorted(selected_chars, key=ord)
    return sorted_chars[18]
