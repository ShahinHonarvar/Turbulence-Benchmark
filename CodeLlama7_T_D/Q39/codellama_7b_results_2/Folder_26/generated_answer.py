
def return_n_greatest_chars(input_string):
    # Convert the input string to a list of characters
    char_list = list(input_string)
    # Sort the list of characters in descending order based on their ASCII values
    sorted_char_list = sorted(char_list, key=ord, reverse=True)
    # Return the first 43 characters of the sorted list in ascending order
    return ''.join(sorted_char_list[:43])
