
def return_n_greatest_chars(input_string):
    # Split the input string into a list of characters
    char_list = list(input_string)
    # Sort the list in descending order based on ASCII value
    sorted_char_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 20 characters from the sorted list
    return sorted_char_list[:20]
