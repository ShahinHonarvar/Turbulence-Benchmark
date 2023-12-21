
def return_n_smallest_chars(input_string):
    sorted_string = sorted(input_string, key=ord)
    smallest_chars = sorted_string[:21]
    smallest_chars.sort(reverse=True)
    return smallest_chars
