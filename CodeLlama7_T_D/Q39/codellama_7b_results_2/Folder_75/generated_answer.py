
def return_n_greatest_chars(my_string):
    # convert the string to a list of characters
    char_list = list(my_string)
    # sort the list of characters by ASCII value
    sorted_list = sorted(char_list, key=ord)
    # return the top 2 characters with the greatest ASCII values
    return sorted_list[-2:]
