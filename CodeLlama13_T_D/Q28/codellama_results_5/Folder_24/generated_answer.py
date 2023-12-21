
def return_nth_smallest_ascii(string):
    # find the 12th smallest ASCII value among characters in string[34:81]
    ascii_values = []
    for char in string[34:81]:
        if char not in ascii_values:
            ascii_values.append(ord(char))
    # sort the list of ASCII values and return the 12th element
    sorted(ascii_values)
    return chr(ascii_values[11])
