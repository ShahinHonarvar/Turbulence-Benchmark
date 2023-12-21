
def return_n_smallest_chars(distinct_chars):
    ascii_char_list = sorted(list(distinct_chars), key=lambda x: ord(x))
    return ascii_char_list[:64]
