
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 51 and 60
    chars = string[51:60]
    # Create a list of ASCII values for each character in the extracted substring
    ascii_values = [ord(char) for char in chars]
    # Sort the list of ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 5th smallest ASCII value in the sorted list
    return sorted_ascii_values[4]
