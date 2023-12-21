
def return_n_smallest_chars(input_string):
    input_string = sorted(input_string, key=ord)[:64]
    input_string.sort(reverse=True)
    return input_string
