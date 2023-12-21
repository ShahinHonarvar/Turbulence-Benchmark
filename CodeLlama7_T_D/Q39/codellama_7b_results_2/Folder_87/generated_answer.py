
def return_n_greatest_chars(my_string):
    # convert the string to a list of characters
    char_list = list(my_string)
    # sort the list of characters by ASCII value in descending order
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # return the top 24 characters from the sorted list
    return sorted_list[:24]
