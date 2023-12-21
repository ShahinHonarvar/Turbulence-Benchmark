
def return_n_smallest_chars(string):
    # Create a list of characters from the given string
    char_list = list(string)
    # Sort the list in descending order based on the ASCII values of the characters
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 44 characters of the sorted list
    return sorted_list[:44]
