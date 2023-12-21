
def return_n_smallest_chars(char_string):
    sorted_chars = sorted(char_string, key=lambda c: ord(c))
    smallest_chars = sorted_chars[:90]
    return sorted(smallest_chars, reverse=True)
