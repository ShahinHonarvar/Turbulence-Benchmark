
def return_n_smallest_chars(input_string):
    char_list = sorted(list(input_string), key=ord)
    smallest_chars = char_list[:47]
    smallest_chars.sort(reverse=True)
    return smallest_chars
