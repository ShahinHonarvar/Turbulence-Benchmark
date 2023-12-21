
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = []
    for char in string:
        if char not in char_list:
            char_list.append(char)
    # Sort the list of characters by their ASCII values
    sorted_list = sorted(char_list, key=ord)
    # Return the 16th smallest ASCII value among those characters in the string that occur between indices 0 to 15, both inclusive.
    return sorted_list[15]
