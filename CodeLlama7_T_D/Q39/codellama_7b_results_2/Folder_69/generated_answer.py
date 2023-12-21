
def return_n_greatest_chars(input_string):
    # Convert the input string to a list of characters
    char_list = list(input_string)

    # Sort the character list in descending order based on their ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)

    # Return the top 65 characters of the sorted list
    return sorted_list[:65]
