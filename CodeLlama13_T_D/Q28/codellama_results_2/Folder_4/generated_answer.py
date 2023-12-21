
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string[9:23]]
    nth_smallest_value = sorted(ascii_values)[3]
    nth_smallest_character = chr(nth_smallest_value)
    return nth_smallest_character
