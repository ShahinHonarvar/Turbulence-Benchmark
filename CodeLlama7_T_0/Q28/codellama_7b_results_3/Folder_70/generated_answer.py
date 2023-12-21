
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Get the indices of the characters between 28 and 54 (inclusive)
    indices = [i for i, x in enumerate(char_list) if 28 <= i <= 54]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(char_list[indices[0]:indices[-1]+1]], key=ord)
    # Return the character with the 14th smallest ASCII value
    return sorted_chars[13]
