
def return_nth_smallest_ascii(string):
    ascii_values = {ord(char): char for char in string}
    sorted_ascii_values = sorted([v for v in ascii_values.keys()])[67:78]
    return ascii_values[sorted_ascii_values[6]]
