
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Sort the list of characters by ASCII value
    sorted_list = sorted(char_list, key=ord)
    # Return the 5th smallest ASCII value
    return sorted_list[4]
