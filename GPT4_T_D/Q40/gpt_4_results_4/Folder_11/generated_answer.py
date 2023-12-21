
def return_n_smallest_chars(char_string):
    sorted_chars = sorted(char_string, key=ord)
    smallest_chars = sorted_chars[:17]
    return smallest_chars
