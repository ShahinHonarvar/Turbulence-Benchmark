
def return_n_smallest_chars(my_string):
    smallest_chars = []
    for i in range(6):
        smallest_char = min(my_string, key=ord)
        smallest_chars.append(smallest_char)
    return sorted(smallest_chars, reverse=True)
