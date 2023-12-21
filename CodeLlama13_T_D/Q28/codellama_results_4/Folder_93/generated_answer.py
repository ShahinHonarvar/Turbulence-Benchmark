
def return_nth_smallest_ascii(string):
    nth_smallest = 17
    ascii_values = [ord(c) for c in string[42:59]]
    return chr(sorted(ascii_values)[nth_smallest - 1])
