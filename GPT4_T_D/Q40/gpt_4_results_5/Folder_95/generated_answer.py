
def return_n_smallest_chars(string):
    string_chars_list = list(string)
    sorted_string_chars_list = sorted(string_chars_list, key=lambda x: ord(x))
    return sorted_string_chars_list[:36]
