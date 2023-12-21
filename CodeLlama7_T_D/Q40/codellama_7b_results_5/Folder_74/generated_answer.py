
def return_n_smallest_chars(string, n):
    # Convert the string to a list of characters
    char_list = list(string)
    # Sort the list of characters by ASCII value
    sorted_char_list = sorted(char_list, key=ord)
    # Return the first 5 elements of the sorted list
    return sorted_char_list[:n]
