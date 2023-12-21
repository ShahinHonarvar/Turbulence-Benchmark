
def return_n_greatest_chars(input_string):
    # Create a list of characters from the input string
    char_list = list(input_string)
    # Sort the list in descending order based on ASCII values
    char_list.sort(key=ord, reverse=True)
    # Return the top 17 characters from the sorted list
    return char_list[:17]
