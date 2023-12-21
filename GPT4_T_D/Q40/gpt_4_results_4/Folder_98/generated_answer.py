
def return_n_smallest_chars(input_string):
    sorted_string = sorted(input_string, key=ord)
    return sorted_string[:68][::-1]
