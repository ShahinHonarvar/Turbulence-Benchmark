def return_n_smallest_chars(str_of_chars):
    n = 54
    smallest_chars = sorted(str_of_chars)[::-1][:n]
    return smallest_chars
