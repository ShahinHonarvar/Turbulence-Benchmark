
def return_n_greatest_chars(string):
    # Create a list of characters in the string
    char_list = list(string)
    # Sort the list in descending order based on ASCII values
    char_list.sort(key=ord, reverse=True)
    # Return the top 11 characters from the sorted list
    return char_list[:11]
