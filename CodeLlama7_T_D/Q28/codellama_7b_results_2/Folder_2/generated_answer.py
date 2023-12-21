
def return_nth_smallest_ascii(string):
    # Create a list of characters in the string
    char_list = list(string)
    # Get the indices of the characters that occur between 48 and 76 (inclusive)
    indices = [i for i, c in enumerate(char_list) if 48 <= ord(c) <= 76]
    # Sort the indices by their corresponding ASCII values
    sorted_indices = sorted(indices, key=lambda x: ord(char_list[x]))
    # Return the nth smallest ASCII value
    return char_list[sorted_indices[4]]
