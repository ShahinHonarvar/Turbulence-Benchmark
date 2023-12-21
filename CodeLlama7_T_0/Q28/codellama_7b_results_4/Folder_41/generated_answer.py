
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Get the indices of the characters that occur between 58 and 85
    indices = [i for i, x in enumerate(char_list) if 58 <= i <= 85]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(char_list[indices[0]:indices[-1]+1]], key=ord)
    # Return the character with the 19th smallest ASCII value
    return sorted_chars[18]
