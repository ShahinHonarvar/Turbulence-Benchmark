
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 25 and 77
    substring = string[25:77]
    # Create a list of ASCII values for each character in the substring
    ascii_values = [ord(c) for c in substring]
    # Sort the list of ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 16th smallest ASCII value from the sorted list
    return sorted_ascii_values[15]
