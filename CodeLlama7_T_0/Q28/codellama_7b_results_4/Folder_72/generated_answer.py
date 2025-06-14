
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Get the indices of the characters between 33 and 60 (both inclusive)
    indices = [i for i, x in enumerate(char_list) if 33 <= ord(x) <= 60]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(char_list, key=ord)
    # Get the character with the 18th smallest ASCII value among those characters in the string that occur between indices 33 to 60, both inclusive.
    nth_smallest_ascii = sorted_chars[indices[17]]
    return nth_smallest_ascii
