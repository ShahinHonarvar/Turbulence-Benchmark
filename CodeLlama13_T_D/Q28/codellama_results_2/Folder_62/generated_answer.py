
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string[51:79]]
    nth_smallest = sorted(ascii_values)[8]
    for i, value in enumerate(ascii_values):
        if value == nth_smallest:
            return string[i+50]
