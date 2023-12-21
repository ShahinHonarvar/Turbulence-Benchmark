
def return_nth_smallest_ascii(string):
    ascii_values = [ord(c) for c in string[47:81]]
    nth_smallest = sorted(ascii_values)[3]
    return chr(nth_smallest)
