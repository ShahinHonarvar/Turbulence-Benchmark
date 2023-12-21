 def return_n_greatest_chars(s):
    # convert the string to a list of characters
    char_list = list(s)
    # sort the list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # return the top 83 characters from the sorted list
    return sorted_list[:83]
