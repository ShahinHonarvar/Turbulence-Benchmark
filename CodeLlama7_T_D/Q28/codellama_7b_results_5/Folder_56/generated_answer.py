
def return_nth_smallest_ascii(string):
    # Get a list of all the characters in the string
    char_list = list(string)
    # Sort the list of characters by ASCII value
    sorted_char_list = sorted(char_list, key=ord)
    # Return the 4th smallest character in the sorted list
    return sorted_char_list[3]
