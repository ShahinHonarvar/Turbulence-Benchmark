
def return_n_greatest_chars(my_string):
    # Create a list of characters from the input string
    char_list = list(my_string)
    # Sort the list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 89 characters from the sorted list
    return sorted_list[:89]
