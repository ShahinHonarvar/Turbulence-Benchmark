
def return_nth_smallest_ascii(string):
    # Extract only the characters between indices 1 and 36
    characters = string[1:37]
    
    # Create a list of ASCII values for the characters
    ascii_values = [ord(char) for char in characters]
    
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_values)
    
    # Return the character corresponding to the 15th smallest ASCII value
    return chr(sorted_ascii_values[14])
