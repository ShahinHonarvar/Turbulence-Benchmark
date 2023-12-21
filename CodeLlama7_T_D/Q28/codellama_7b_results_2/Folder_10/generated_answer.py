
def return_nth_smallest_ascii(string):
    # Extract the characters between indices 38 and 82
    char_list = string[38:82+1]
    # Sort the list of characters by their ASCII values
    sorted_list = sorted(char_list, key=ord)
    # Return the character with the 20th smallest ASCII value
    return sorted_list[19]
