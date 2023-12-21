
def return_nth_smallest_ascii(string):
    # Create a list of characters that occur between indices 24 and 71
    char_list = []
    for i in range(24, 72):
        if string[i] not in char_list:
            char_list.append(string[i])
    # Sort the list of characters by their ASCII values
    sorted_list = sorted(char_list, key=ord)
    # Return the character with the 8th smallest ASCII value
    return sorted_list[7]
