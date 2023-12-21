
def return_nth_smallest_ascii(string):
    # Create a dictionary to store the ASCII values of each character in the string
    ascii_values = {}
    for char in string:
        if char not in ascii_values:
            ascii_values[char] = ord(char)

    # Sort the ASCII values in ascending order

    sorted_ascii_values = sorted(ascii_values.values())

    # Return the 13th smallest ASCII value

    return sorted_ascii_values[12]
