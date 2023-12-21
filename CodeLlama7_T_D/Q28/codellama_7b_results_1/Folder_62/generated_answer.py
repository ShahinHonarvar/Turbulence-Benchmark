
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 51 and 78
    char_list = string[51:79]
    # Initialize a dictionary to store the ASCII values of each character
    ascii_dict = {}
    # Iterate through the list of characters
    for char in char_list:
        # Get the ASCII value of the current character
        ascii_value = ord(char)
        # Add the ASCII value and its corresponding character to the dictionary
        ascii_dict[ascii_value] = char
    # Sort the dictionary by key (ASCII value) in descending order
    sorted_dict = sorted(ascii_dict.items(), key=lambda x: x[0], reverse=True)
    # Get the 9th smallest ASCII value from the sorted dictionary
    nth_smallest_ascii = sorted_dict[8][0]
    # Return the character corresponding to the 9th smallest ASCII value
    return ascii_dict[nth_smallest_ascii]
