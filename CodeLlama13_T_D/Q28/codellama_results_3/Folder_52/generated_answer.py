
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string if 46 <= ord(char) <= 72]
    nth_smallest = sorted(ascii_values)[15]
    return chr(nth_smallest)
