
def return_n_greatest_chars(string, n=58):
    # create a list of characters in the string
    char_list = list(string)
    # sort the list in descending order based on ASCII values
    char_list.sort(key=ord, reverse=True)
    # return the top n characters from the sorted list
    return char_list[:n]
