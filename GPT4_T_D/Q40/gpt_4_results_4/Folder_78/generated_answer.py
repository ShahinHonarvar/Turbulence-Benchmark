
def return_n_smallest_chars(char_string):
    sorted_char_list = sorted(char_string, key=ord)
    smallest_chars = sorted_char_list[:43]
    smallest_chars.sort(reverse=True)
    return smallest_chars
