
def return_n_smallest_chars(string, n):
    # convert string to a list of characters
    char_list = list(string)
    # sort the list in ascending order based on ASCII values
    sorted_list = sorted(char_list, key=ord)
    # return the first n elements of the sorted list
    return sorted_list[:n]
