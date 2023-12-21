
def return_n_smallest_chars(string, n):
    # create a list of characters from the string
    char_list = list(string)
    # sort the list in ascending order based on ASCII values
    char_list.sort(key=ord)
    # return the first n characters of the sorted list
    return char_list[:n]
