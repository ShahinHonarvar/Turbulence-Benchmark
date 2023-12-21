 def return_n_smallest_chars(string):
    # convert string to a list of characters
    char_list = list(string)
    # sort the list in descending order based on ASCII values
    char_list.sort(key=ord, reverse=True)
    # return the first 56 characters of the sorted list
    return char_list[:56]
