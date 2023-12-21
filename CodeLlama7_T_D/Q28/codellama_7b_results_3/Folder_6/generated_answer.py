
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string
    start_index = string.find('a')
    end_index = string.rfind('z')
    # Initialize a list to store the ASCII values of the characters
    ascii_values = []
    # Iterate through the characters in the string and append their ASCII values to the list
    for char in string:
        ascii_values.append(ord(char))
    # Sort the list of ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 11th smallest ASCII value among those characters that occur between indices 14 to 54, both inclusive.
    return sorted_ascii_values[10]
