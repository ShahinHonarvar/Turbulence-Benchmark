
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Find the ASCII values of all the characters in the list
    ascii_values = [ord(char) for char in char_list]
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 4th smallest ASCII value among the sorted values
    return chr(sorted_ascii_values[3])
