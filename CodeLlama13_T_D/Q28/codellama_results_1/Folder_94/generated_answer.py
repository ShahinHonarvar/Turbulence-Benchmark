
def return_nth_smallest_ascii(string):
    ascii_values = [ord(c) for c in string if 6 <= ord(c) <= 58]
    nth_smallest_value = sorted(ascii_values)[19 - 1]
    return chr(nth_smallest_value)
