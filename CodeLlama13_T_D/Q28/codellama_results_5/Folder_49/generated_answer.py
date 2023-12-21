
def return_nth_smallest_ascii(string):
    ascii_values = [ord(c) for c in string[20:81]]
    nth_smallest = sorted(ascii_values)[10]
    for char in string:
        if ord(char) == nth_smallest:
            return char
