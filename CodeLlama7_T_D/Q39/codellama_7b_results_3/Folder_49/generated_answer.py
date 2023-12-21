
def return_n_greatest_chars(my_string):
    # Convert the string to a list of characters
    char_list = list(my_string)
    # Sort the list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 76 characters from the sorted list
    return sorted_list[:76]
