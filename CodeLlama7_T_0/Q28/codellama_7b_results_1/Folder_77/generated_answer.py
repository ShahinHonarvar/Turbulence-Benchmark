
def return_nth_smallest_ascii(string):
    # Find the indices of the characters in the string that occur between indices 63 and 76, both inclusive
    start_index = string.find('a', 63)
    end_index = string.rfind('z', 76)
    # Create a list of all the characters in the string that occur between the found indices
    char_list = []
    for i in range(start_index, end_index + 1):
        char_list.append(string[i])
    # Sort the list of characters by their ASCII values
    sorted_list = sorted(char_list, key=ord)
    # Return the character with the 14th smallest ASCII value among those characters in the string that occur between indices 63 to 76, both inclusive.
    return sorted_list[13]
