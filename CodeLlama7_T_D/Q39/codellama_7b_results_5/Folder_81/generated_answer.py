
def return_n_greatest_chars(string, n=64):
    # Create a list of characters from the given string
    char_list = list(string)
    # Sort the list of characters in ascending order based on their ASCII values
    sorted_char_list = sorted(char_list, key=ord)
    # Return the first n elements of the sorted list
    return sorted_char_list[:n]
