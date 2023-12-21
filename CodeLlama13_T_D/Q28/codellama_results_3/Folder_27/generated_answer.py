
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string[33:86]]
    nth_smallest_ascii = sorted(ascii_values)[12]
    for char in string[33:86]:
        if ord(char) == nth_smallest_ascii:
            return char
