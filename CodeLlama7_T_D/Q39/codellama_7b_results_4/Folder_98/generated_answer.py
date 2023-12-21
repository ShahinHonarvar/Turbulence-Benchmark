
def return_n_greatest_chars(string):
    # Create a list of all characters in the string
    char_list = list(string)
    # Sort the list in descending order based on ASCII values
    sorted_char_list = sorted(char_list, key=ord, reverse=True)
    # Return the first 68 characters of the sorted list
    return ''.join(sorted_char_list[:68])
