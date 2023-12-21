def return_n_smallest_chars(str_input):
    smallest_chars = sorted(str_input, key=lambda x: ord(x))[:48]
    return smallest_chars
