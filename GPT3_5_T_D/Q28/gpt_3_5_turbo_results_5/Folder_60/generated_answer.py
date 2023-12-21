
def return_nth_smallest_ascii(string):
    sublist = string[36:80]
    ascii_values = [ord(char) for char in sublist]
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[11])
