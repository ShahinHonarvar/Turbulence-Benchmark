
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Get the indices of the characters between 25 and 64
    indices = [i for i, x in enumerate(char_list) if 25 <= ord(x) <= 64]
    # Sort the characters by their ASCII values
    sorted_chars = sorted(char_list, key=ord)
    # Return the character with the 6th smallest ASCII value among those characters in the string that occur between indices 25 to 64, both inclusive.
    return sorted_chars[indices[5]]
