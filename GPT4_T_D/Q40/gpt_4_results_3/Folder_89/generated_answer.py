
def return_n_smallest_chars(char_string):
    sorted_chars = sorted(char_string, key=ord)
    return sorted_chars[:55]
