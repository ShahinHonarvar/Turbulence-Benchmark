
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Get the indices of the characters between 60 and 83
    indices = [i for i, x in enumerate(char_list) if 60 <= ord(x) <= 83]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(char_list, key=ord)
    # Get the 14th smallest ASCII value among the characters between indices 60 and 83
    nth_smallest = sorted_chars[indices[13]]
    return nth_smallest
