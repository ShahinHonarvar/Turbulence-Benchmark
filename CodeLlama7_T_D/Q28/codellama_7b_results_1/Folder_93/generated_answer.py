
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Get the indices of the characters in the list that occur between indices 42 and 59, both inclusive.
    indices = [i for i, x in enumerate(char_list) if 42 <= i <= 59]
    # Get the ASCII values of the characters at these indices.
    ascii_values = [ord(x) for x in char_list[indices]]
    # Return the character with the 17th smallest ASCII value among these characters.
    return chr(sorted(ascii_values)[16]))
