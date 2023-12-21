
def return_n_greatest_chars(s, n):
    # convert string to a list of characters
    char_list = list(s)
    # sort the list in descending order based on ASCII values
    char_list.sort(key=ord, reverse=True)
    # return the top n elements of the sorted list
    return char_list[:n]
