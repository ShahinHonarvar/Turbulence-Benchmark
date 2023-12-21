
def return_n_greatest_chars(string):
    # convert the string to a list of characters
    char_list = list(string)
    # sort the list in descending order based on ASCII value
    char_list.sort(key=ord, reverse=True)
    # return the first 48 characters of the sorted list
    return ''.join(char_list[:48])
