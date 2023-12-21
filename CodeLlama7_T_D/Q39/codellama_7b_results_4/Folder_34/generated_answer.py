
def return_n_greatest_chars(string, n=9):
    # Create a list of all characters in the string
    char_list = list(string)
    # Sort the list of characters in descending order based on their ASCII values
    char_list.sort(key=ord, reverse=True)
    # Return the first n elements of the sorted list
    return char_list[:n]
