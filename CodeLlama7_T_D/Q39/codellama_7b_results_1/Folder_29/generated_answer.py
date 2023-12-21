
def return_n_greatest_chars(string):
    # Create a list of all characters in the string
    char_list = list(string)
    # Sort the list in descending order based on ASCII values
    char_list.sort(key=ord, reverse=True)
    # Return the first 23 elements of the sorted list
    return char_list[:23]
