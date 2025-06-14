
def return_n_greatest_chars(input_string):
    # Split the input string into a list of individual characters
    char_list = list(input_string)
    # Sort the character list in descending order based on their ASCII values
    sorted_char_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 57 characters from the sorted list
    return sorted_char_list[:57]
