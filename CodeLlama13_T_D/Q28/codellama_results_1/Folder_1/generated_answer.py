
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string if 21 <= ord(char) <= 59]
    ascii_values.sort()
    nth_smallest = ascii_values[10]
    return chr(nth_smallest)
