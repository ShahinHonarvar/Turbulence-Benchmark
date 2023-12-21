
def return_n_smallest_chars(string):
    # Convert the string to a list of characters
    char_list = list(string)
    # Sort the list in descending order based on the ASCII values of the characters
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the first 59 characters of the sorted list
    return sorted_list[:59]
