
def return_nth_smallest_ascii(string):
    # Create a list of characters between indices 40 and 60
    char_list = string[40:61]
    # Sort the list in ascending order based on ASCII value
    char_list.sort(key=ord)
    # Return the character with the 19th smallest ASCII value
    return char_list[18]
