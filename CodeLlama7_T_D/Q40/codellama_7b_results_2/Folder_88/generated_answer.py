
def return_n_smallest_chars(string, n):
    # create a list of all characters in the string
    char_list = list(string)
    # sort the list in ascending order based on ASCII values
    char_list.sort(key=ord)
    # return the first 84 characters of the sorted list
    return char_list[:n]
