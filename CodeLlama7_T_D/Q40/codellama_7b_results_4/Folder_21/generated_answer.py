
def return_n_smallest_chars(string):
    # create a list of all characters in the string
    char_list = list(string)
    # sort the list in descending order based on ASCII values
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # return the first 44 characters of the sorted list
    return sorted_list[:44]
