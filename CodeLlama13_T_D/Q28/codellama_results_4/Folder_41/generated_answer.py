
def return_nth_smallest_ascii(string):
    ascii_values = {ord(char): char for char in string}
    indices = range(58, 86)
    nth_smallest = sorted([ascii_values[i] for i in indices])[19]
    return nth_smallest
