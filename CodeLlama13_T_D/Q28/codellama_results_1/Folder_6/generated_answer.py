
def return_nth_smallest_ascii(string):
    # Get the characters between indices 14 and 54, both inclusive
    chars = string[13:55]
    
    # Create a dictionary to store the ASCII values of each character
    ascii_values = {}
    for char in chars:
        ascii_values[char] = ord(char)
    
    # Sort the characters by their ASCII values
    sorted_chars = sorted(ascii_values.items(), key=lambda x: x[1])
    
    # Return the character with the 11th smallest ASCII value
    return sorted_chars[10][0]
