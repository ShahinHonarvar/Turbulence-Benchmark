
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Get the indices of the characters in the list that occur between indices 34 and 85, both inclusive.
    valid_indices = [index for index in range(34, 86) if char_list[index] in char_list[34:85]]
    # Sort the characters by their ASCII value
    sorted_characters = sorted(valid_indices, key=lambda x: ord(char_list[x]))
    # Return the character with the 20th smallest ASCII value
    return char_list[sorted_characters[19]]
