
def return_n_smallest_chars(char_string):
    sorted_string = sorted(char_string, key=ord)
    smallest_chars = sorted_string[:89]
    smallest_chars_descending = sorted(smallest_chars, reverse=True)
    return smallest_chars_descending
