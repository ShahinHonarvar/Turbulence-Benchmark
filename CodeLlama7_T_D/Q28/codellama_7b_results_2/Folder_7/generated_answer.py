
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = []
    for char in string:
        if char not in char_list:
            char_list.append(char)
    # Sort the list of characters by their ASCII value
    sorted_list = sorted(char_list, key=ord)
    # Return the character with the 17th smallest ASCII value
    return sorted_list[16]
