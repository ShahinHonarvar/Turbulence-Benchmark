
def return_n_smallest_chars(input_string):
    input_string = sorted(set(input_string))
    smallest_chars = input_string[:29]
    smallest_chars = sorted(smallest_chars, reverse=True)
    return smallest_chars
