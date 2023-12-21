
def return_nth_smallest_ascii(string):
    new_string = string[50:77]
    unique_chars = list(set(new_string))
    sorted_chars = sorted(unique_chars)
    return sorted_chars[10]
