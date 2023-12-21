
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 5 and 82 from the string
    characters = string[5:82]
    # Create a list of ASCII values for each character in the string
    ascii_values = [ord(char) for char in characters]
    # Sort the list of ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 16th smallest ASCII value from the sorted list
    return sorted_ascii_values[15]
