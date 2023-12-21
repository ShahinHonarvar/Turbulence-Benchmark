 def return_n_smallest_chars(string):
    # convert the string to a list of characters
    char_list = list(string)
    # sort the list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # return the first 47 characters of the sorted list
    return sorted_list[:47]
