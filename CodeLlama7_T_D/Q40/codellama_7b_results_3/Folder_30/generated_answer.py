
def return_n_smallest_chars(string, n=72):
    # Create a list of all characters in the string
    char_list = list(string)

    # Sort the list in ascending order based on the ASCII values of the characters
    sorted_char_list = sorted(char_list, key=ord)

    # Return the first n elements of the sorted list
    return sorted_char_list[:n]
