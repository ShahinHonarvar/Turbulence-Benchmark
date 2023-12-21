
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Create a dictionary to store the ASCII values of each character
    ascii_dict = {}
    # Iterate through the list of characters and store their ASCII values in the dictionary
    for char in char_list:
        ascii_dict[char] = ord(char)
    # Sort the dictionary by value (ASCII values)
    sorted_ascii_dict = sorted(ascii_dict.items(), key=lambda x: x[1])
    # Return the 8th smallest ASCII value
    return sorted_ascii_dict[7][0]
