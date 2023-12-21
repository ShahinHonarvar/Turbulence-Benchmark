
def return_n_greatest_chars(input_string):
    # Convert the input string to a list of characters
    char_list = list(input_string)
    # Sort the character list in descending order based on ASCII values
    sorted_char_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 47 characters from the sorted list
    return sorted_char_list[:47]
