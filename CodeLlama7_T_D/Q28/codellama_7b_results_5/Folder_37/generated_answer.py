
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string
    indices = []
    for char in string:
        indices.append(string.index(char))

    # Get the ASCII values of the characters

    ascii_values = []

    for index in indices:

        ascii_values.append(ord(string[index]))


    # Sort the ASCII values in ascending order

    sorted_ascii_values = sorted(ascii_values)


    # Return the 15th smallest ASCII value

    return sorted_ascii_values[14]
