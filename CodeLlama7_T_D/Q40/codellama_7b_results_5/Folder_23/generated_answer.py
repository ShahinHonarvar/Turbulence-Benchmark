
def return_n_smallest_chars(my_string):
    smallest_chars = []
    for char in my_string:
        if len(smallest_chars) < 46:
            smallest_chars.append(char)
    return sorted(smallest_chars)
