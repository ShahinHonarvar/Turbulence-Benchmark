
def return_nth_smallest_ascii(string):
    ascii_values = [ord(c) for c in string[47:80]]
    nth_smallest_ascii = sorted(set(ascii_values))[3]
    for char in string:
        if ord(char) == nth_smallest_ascii:
            return char
