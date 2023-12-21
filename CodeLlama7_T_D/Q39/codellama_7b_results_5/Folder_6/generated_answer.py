
def return_n_greatest_chars(string):
    # Convert the string to a list of characters
    char_list = list(string)

    # Sort the list in descending order based on ASCII values
    sorted_char_list = sorted(char_list, key=ord, reverse=True)

    # Return the top 47 characters of the sorted list
    return sorted_char_list[:47]
