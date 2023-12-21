def return_n_smallest_chars(str_of_chars):
    return [c for c in str_of_chars if c in set(str_of_chars)][::-1][:70]
