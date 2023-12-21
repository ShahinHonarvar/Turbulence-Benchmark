
def return_nth_smallest_ascii(string):
    ascii_values = [ord(c) for c in string[37:60]]
    nth_smallest_ascii = sorted(ascii_values)[5]
    for char in string:
        if ord(char) == nth_smallest_ascii:
            return char
