
def return_nth_smallest_ascii(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Sort the list of characters based on their ASCII values
    sorted_list = sorted(char_list, key=ord)
    # Return the 15th character in the sorted list
    return sorted_list[14]
