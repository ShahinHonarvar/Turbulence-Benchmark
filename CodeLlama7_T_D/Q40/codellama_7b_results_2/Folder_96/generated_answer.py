
def return_n_smallest_chars(string, n):
    # Convert string to a list of characters
    char_list = list(string)
    # Sort the list in descending order based on ASCII values
    char_list.sort(key=ord, reverse=True)
    # Return the top 20 characters from the sorted list
    return char_list[:n]
