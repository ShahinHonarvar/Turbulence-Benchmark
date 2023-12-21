
def return_nth_smallest_ascii(string):
    ascii_values = [ord(c) for c in string[34:81]]
    nth_smallest = sorted(ascii_values)[11]
    return chr(nth_smallest)
