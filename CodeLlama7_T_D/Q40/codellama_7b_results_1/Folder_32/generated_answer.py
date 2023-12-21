
def return_n_smallest_chars(string, n=8):
    # Convert string to a list of characters
    char_list = list(string)
    # Sort the list in ascending order based on ASCII values
    sorted_char_list = sorted(char_list, key=ord)
    # Return the first 8 characters of the sorted list
    return sorted_char_list[:n]
