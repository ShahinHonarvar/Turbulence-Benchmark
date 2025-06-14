
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Get the indices of the characters that occur between 51 and 78
    indices = [i for i, x in enumerate(char_list) if 51 <= i <= 78]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(char_list[indices[0]:indices[-1]+1]], key=ord)
    # Return the character with the 9th smallest ASCII value
    return sorted_chars[8]
