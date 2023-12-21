
def return_n_smallest_chars(input_string):
    sorted_string = sorted(input_string, key=lambda x: ord(x))
    smallest_chars = sorted_string[:43]
    return smallest_chars
