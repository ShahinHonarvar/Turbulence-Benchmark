
def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string, key=lambda x: ord(x))
    top_61_chars = sorted_chars[:61]
    top_61_chars_descending = top_61_chars[::-1]
    return top_61_chars_descending
