
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Create a dictionary to store the ASCII values and their indices
    ascii_dict = {}
    # Iterate over the characters in the list
    for i, char in enumerate(char_list):
        # Add the ASCII value and its index to the dictionary
        ascii_dict[ord(char)] = i
    # Get the 9th smallest ASCII value from the dictionary
    nth_smallest_ascii = sorted(ascii_dict.keys())[8]
    # Return the character with the 9th smallest ASCII value
    return char_list[ascii_dict[nth_smallest_ascii]]
