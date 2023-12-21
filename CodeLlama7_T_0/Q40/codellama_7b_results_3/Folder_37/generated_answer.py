
def return_n_smallest_chars(string):
    # Create a list of all characters in the string
    char_list = list(string)
    # Sort the list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 26 characters from the sorted list
    return sorted_list[:26]
