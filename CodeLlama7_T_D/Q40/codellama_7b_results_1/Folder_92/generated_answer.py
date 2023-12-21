
def return_n_smallest_chars(string, n):
    # convert the string to a list of characters
    char_list = list(string)
    # sort the list of characters in ascending order based on their ASCII values
    sorted_char_list = sorted(char_list, key=ord)
    # return the first 63 characters of the sorted list
    return sorted_char_list[:n]
