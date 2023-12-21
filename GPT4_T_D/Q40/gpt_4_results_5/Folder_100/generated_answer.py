
def return_n_smallest_chars(input_string):
    sorted_chars = sorted(input_string, key=lambda char: ord(char))
    return sorted_chars[:72][::-1]
