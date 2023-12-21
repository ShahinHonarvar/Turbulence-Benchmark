import sys
def return_n_smallest_chars(str_of_chars):
    return sorted(list(str_of_chars), key=lambda x: ord(x))[:8]
