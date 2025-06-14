
def return_n_greatest_chars(input_string):
    # Split the input string into a list of individual characters
    char_list = list(input_string)
    # Sort the list of characters by their ASCII values in descending order
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 73 characters from the sorted list
    return sorted_list[:73]
