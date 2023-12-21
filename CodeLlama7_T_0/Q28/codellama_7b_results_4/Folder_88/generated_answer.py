
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Get the indices of the characters between 38 and 64
    indices = [i for i, x in enumerate(char_list) if 38 <= ord(x) <= 64]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(char_list, key=ord)
    # Get the character with the 14th smallest ASCII value
    nth_smallest = sorted_chars[indices[13]]
    return nth_smallest
