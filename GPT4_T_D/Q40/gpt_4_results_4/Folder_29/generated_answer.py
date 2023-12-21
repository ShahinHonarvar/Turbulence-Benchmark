
def return_n_smallest_chars(char_string):
    sorted_char_list = sorted(char_string, key=ord)
    n_smallest_chars = sorted_char_list[:23]
    n_smallest_chars.sort(reverse=True)
    return n_smallest_chars
