 def return_n_smallest_chars(string):
    # Convert string to a list of characters
    char_list = list(string)
    # Sort the list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 49 characters from the sorted list
    return sorted_list[:49]
