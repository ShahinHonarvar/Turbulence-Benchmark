
def return_n_greatest_chars(string):
    # convert the string to a list of characters
    char_list = list(string)
    # sort the list in descending order based on ASCII values
    sorted_char_list = sorted(char_list, key=ord, reverse=True)
    # return the first 79 elements of the sorted list
    return sorted_char_list[:79]
