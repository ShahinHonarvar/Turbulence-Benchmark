
def return_n_greatest_chars(string):
    # Split the string into a list of characters
    char_list = list(string)

    # Sort the list of characters in descending order based on their ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)

    # Return the top 21 characters from the sorted list
    return sorted_list[:21]
