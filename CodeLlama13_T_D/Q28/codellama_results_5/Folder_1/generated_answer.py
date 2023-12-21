
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string[21:60]]
    nth_smallest = sorted(set(ascii_values))[11]
    return chr(nth_smallest)
