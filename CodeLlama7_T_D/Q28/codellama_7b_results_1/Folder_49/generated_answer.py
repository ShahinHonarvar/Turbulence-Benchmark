
def return_nth_smallest_ascii(string):
    # Create a list of characters in the given string
    char_list = list(string)
    # Get the indices of the characters that occur between 20 and 80
    indices = [i for i, x in enumerate(char_list) if 20 <= i <= 80]
    # Sort the list of characters based on their ASCII values
    sorted_char_list = sorted(char_list, key=ord)
    # Get the character with the 11th smallest ASCII value among those that occur between indices 20 to 80
    nth_smallest_ascii = sorted_char_list[indices[10]]
    return nth_smallest_ascii
