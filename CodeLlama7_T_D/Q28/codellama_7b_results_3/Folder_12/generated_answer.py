
def return_nth_smallest_ascii(string):
    # Get the characters that occur between indices 3 and 26
    char_list = string[3:27]
    # Sort the list of characters by their ASCII values
    sorted_list = sorted(char_list, key=ord)
    # Return the character with the 5th smallest ASCII value
    return sorted_list[4]
