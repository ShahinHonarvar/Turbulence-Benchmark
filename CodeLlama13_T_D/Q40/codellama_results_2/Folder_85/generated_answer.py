
def return_n_smallest_chars(distinct_chars):
    char_list = list(distinct_chars)
    sorted_char_list = sorted(char_list, key=ord)
    return sorted_char_list[:85]
