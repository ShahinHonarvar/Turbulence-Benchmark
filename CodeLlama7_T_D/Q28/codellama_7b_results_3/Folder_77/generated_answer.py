
def return_nth_smallest_ascii(string):
    # Get the indices of the characters in the string that occur between 63 and 76
    start = string.index('<') + 1
    end = string.index('>') - 1
    # Get the list of characters in the string between these indices
    char_list = string[start:end]
    # Sort the list of characters by their ASCII values
    sorted_list = sorted(char_list, key=ord)
    # Return the character with the 14th smallest ASCII value
    return sorted_list[13]
