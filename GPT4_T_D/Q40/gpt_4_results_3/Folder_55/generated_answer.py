
def return_n_smallest_chars(input_string):
    sorted_string = sorted(input_string, key=lambda x: ord(x))[:75]
    sorted_string.reverse()
    return sorted_string
