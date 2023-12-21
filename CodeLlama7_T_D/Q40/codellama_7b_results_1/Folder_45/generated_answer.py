
def return_n_smallest_chars(string):
    # Create a list of all characters in the string
    char_list = list(string)
    # Sort the list in ascending order based on ASCII values
    char_list.sort(key=ord)
    # Return the first 52 characters of the sorted list
    return char_list[:52]
