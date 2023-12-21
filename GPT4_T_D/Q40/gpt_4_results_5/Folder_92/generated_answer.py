
def return_n_smallest_chars(input_string):
    ascii_vals = [(char, ord(char)) for char in input_string]
    sorted_vals = sorted(ascii_vals, key=lambda x: x[1])
    smallest_63_chars = [char for char, _ in sorted_vals[:63]]
    return smallest_63_chars
