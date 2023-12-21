
def return_nth_smallest_ascii(s):
    # Get the indices of the characters in the string
    indices = []
    for i in range(len(s)):
        if s[i] not in indices:
            indices.append(i)

    # Get the ASCII values of the characters at the specified indices
    ascii_values = []
    for i in indices:
        ascii_values.append(ord(s[i]))

    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)

    # Get the 11th smallest ASCII value
    nth_smallest_ascii_value = sorted_ascii_values[10]

    # Return the character with the 11th smallest ASCII value
    return chr(nth_smallest_ascii_value)
