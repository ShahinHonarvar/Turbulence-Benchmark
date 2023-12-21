
def return_n_smallest_chars(string, n):
    # convert the string to a list of characters
    char_list = list(string)
    # sort the list in ascending order based on the ASCII values
    sorted_list = sorted(char_list, key=ord)
    # return the first 31 characters of the sorted list
    return sorted_list[:n]
