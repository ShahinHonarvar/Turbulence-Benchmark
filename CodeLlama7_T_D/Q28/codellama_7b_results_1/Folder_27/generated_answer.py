
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string that occur between indices 33 and 85, both inclusive
    char_list = []
    for i in range(33, 86):
        if string[i] not in char_list:
            char_list.append(string[i])
    # Sort the list of characters by their ASCII values
    sorted_list = sorted(char_list, key=ord)
    # Return the character with the 13th smallest ASCII value
    return sorted_list[12]
