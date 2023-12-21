
def return_n_smallest_chars(my_string):
    # Create a list of all characters in the string
    char_list = list(my_string)
    # Sort the list in descending order based on ASCII value
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the first 16 characters of the sorted list
    return sorted_list[:16]
