
def return_nth_smallest_ascii(string):
    # Create a list of all the characters in the string
    char_list = list(string)
    # Sort the list of characters by their ASCII values
    sorted_list = sorted(char_list, key=ord)
    # Return the 6th smallest ASCII value among the characters in the sorted list
    return sorted_list[5:10]
