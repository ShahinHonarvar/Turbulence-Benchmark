
def return_n_smallest_chars(str):
    # Convert the string to a list of characters
    char_list = list(str)
    # Sort the list of characters in descending order based on their ASCII values
    sorted_char_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 28 characters from the sorted list
    return sorted_char_list[:28]
