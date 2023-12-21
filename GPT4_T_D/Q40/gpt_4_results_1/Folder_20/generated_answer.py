
def return_n_smallest_chars(input_string):
    sorted_chars = sorted(list(input_string), key=ord)[:40]
    return sorted_chars
