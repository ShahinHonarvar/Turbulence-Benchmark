
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Get the indices of the characters between 32 and 67 (inclusive)
    indices = [i for i, x in enumerate(char_list) if 32 <= ord(x) <= 67]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(char_list, key=ord)
    # Get the character with the 12th smallest ASCII value among those characters in the string that occur between indices 32 to 67, both inclusive.
    nth_smallest_ascii = sorted_chars[indices[11]]
    return nth_smallest_ascii
