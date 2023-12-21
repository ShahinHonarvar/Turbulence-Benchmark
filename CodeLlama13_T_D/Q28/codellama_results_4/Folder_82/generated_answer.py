
def return_nth_smallest_ascii(string):
    ascii_values = {ord(c): c for c in string}
    sorted_keys = sorted(ascii_values)
    nth_key = sorted_keys[14]
    return ascii_values[nth_key]
