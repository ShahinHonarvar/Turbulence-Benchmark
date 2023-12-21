
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string that occur between 21 and 59
    start_index = string.find('a', 21)
    end_index = string.find('z', 59)
    # Initialize a list to store the ASCII values of the characters in the string
    ascii_values = []
    # Loop through the indices and append the corresponding ASCII value to the list
    for i in range(start_index, end_index + 1):
        ascii_values.append(ord(string[i]))
    # Sort the list of ASCII values
    ascii_values.sort()
    # Return the character with the 11th smallest ASCII value among those characters in the string that occur between indices 21 to 59, both inclusive
    return chr(ascii_values[10])
