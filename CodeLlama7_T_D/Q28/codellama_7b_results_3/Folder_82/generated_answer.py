
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Create a dictionary to store the ASCII values of each character
    ascii_dict = {}
    # Iterate through the list of characters and add their ASCII values to the dictionary
    for char in char_list:
        if char not in ascii_dict:
            ascii_dict[char] = ord(char)
    # Sort the ASCII values in ascending order
    sorted_ascii_values = sorted(ascii_dict.values())
    # Return the 15th smallest ASCII value
    return sorted_ascii_values[14]
