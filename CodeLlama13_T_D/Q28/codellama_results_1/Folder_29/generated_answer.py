
def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string[5:11]]
    nth_smallest = sorted(ascii_values)[5]
    return chr(nth_smallest)
