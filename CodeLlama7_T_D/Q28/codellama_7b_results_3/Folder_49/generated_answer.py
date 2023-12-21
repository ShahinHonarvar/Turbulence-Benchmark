
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 20 and 80
    sub_string = string[20:81]
    # Create a list of ASCII values for each character in the sub-string
    ascii_values = [ord(char) for char in sub_string]
    # Sort the list in ascending order
    sorted_ascii_values = sorted(ascii_values)
    # Return the 11th smallest ASCII value from the sorted list
    return sorted_ascii_values[10]
