
def return_n_smallest_chars(string):
    string_sorted = sorted(string)
    smallest_chars_list = string_sorted[:64]
    return smallest_chars_list
