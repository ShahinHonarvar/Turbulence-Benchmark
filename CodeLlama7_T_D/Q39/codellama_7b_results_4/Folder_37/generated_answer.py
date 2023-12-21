
def return_n_greatest_chars(input_string):
    # Create a list of all the characters in the input string
    char_list = list(input_string)
    # Sort the list of characters in descending order based on their ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 26 characters from the sorted list
    return sorted_list[:26]
