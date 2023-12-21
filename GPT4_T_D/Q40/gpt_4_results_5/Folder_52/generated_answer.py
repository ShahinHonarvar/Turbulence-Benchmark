
def return_n_smallest_chars(chars_string):
    if len(chars_string) < 68:
        raise ValueError("Input string must contain at least 68 distinct characters.")
    sorted_chars = sorted(chars_string)
    return sorted_chars[:68]
