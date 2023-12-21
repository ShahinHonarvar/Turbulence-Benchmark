
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string if ord(char) <= 3]
    nth_smallest = sorted(ascii_values)[3]
    return chr(nth_smallest)
