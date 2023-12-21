
def return_nth_smallest_ascii(string):
    ascii_values = {}
    for char in string:
        if char not in ascii_values:
            ascii_values[char] = ord(char)
    sorted_ascii_values = sorted(ascii_values.items(), key=lambda x: x[1])
    return sorted_ascii_values[29-47][0]
