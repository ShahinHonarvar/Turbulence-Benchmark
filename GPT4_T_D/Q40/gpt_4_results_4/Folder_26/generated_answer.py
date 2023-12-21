
def return_n_smallest_chars(input_string):
    sorted_string = sorted(input_string, key=lambda char: ord(char))
    return sorted_string[:43]
