
def return_nth_smallest_ascii(string):
    # Create a list of unique characters in the string
    unique_chars = set(string)
    # Initialize a dictionary to store the ASCII values of each character
    ascii_values = {}
    # Iterate over each character in the string
    for char in unique_chars:
        # Get the ASCII value of the current character
        ascii_value = ord(char)
        # Add the ASCII value to the dictionary with the character as the key
        ascii_values[char] = ascii_value
    # Sort the dictionary by the ASCII values of each character
    sorted_values = sorted(ascii_values.items(), key=lambda x: x[1])
    # Return the 13th smallest ASCII value
    return sorted_values[12][1]
