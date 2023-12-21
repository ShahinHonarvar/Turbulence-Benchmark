
def return_n_smallest_chars(string):
    # Create a list of characters from the input string
    char_list = list(string)
    # Sort the list in descending order based on ASCII value
    sorted_char_list = sorted(char_list, key=ord, reverse=True)
    # Return the first 59 characters of the sorted list
    return sorted_char_list[:59]
