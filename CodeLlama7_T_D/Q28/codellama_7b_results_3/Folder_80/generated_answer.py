
def return_nth_smallest_ascii(string):
    # Create a list of the characters in the string
    char_list = list(string)
    # Sort the list of characters by ASCII value
    sorted_list = sorted(char_list, key=ord)
    # Return the 14th character in the sorted list
    return sorted_list[13]
