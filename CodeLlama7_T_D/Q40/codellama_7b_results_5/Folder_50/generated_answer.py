
def return_n_smallest_chars(string, n):
    # Create a list of characters in the given string
    char_list = list(string)

    # Sort the list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)

    # Return the first 16 characters of the sorted list
    return sorted_list[:n]
