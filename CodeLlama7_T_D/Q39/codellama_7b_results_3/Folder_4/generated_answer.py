
def return_n_greatest_chars(string, n):
    # Convert string to list of characters
    char_list = list(string)
    # Sort list in descending order based on ASCII values
    char_list.sort(key=ord, reverse=True)
    # Return the first n elements of the sorted list
    return char_list[:n]
