
def return_nth_smallest_ascii(string):
    # Find the indices of the characters in the string that occur between indices 28 and 54 (both inclusive)
    start_index = string.find(chr(28))
    end_index = string.rfind(chr(54)))
    # Get a list of all the characters in the string that occur between these indices
    char_list = string[start_index:end_index + 1]
    # Sort the list of characters by their ASCII values
    sorted_char_list = sorted(char_list, key=lambda x: ord(x))
    # Return the character with the 14th smallest ASCII value among these characters
    return sorted_char_list[13]
