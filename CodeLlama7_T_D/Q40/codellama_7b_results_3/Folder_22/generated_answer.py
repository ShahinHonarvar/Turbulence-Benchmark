
def return_n_smallest_chars(string):
    # sort the characters in the string by their ASCII values
    sorted_chars = sorted(string, key=ord)
    # create a list of exactly 76 characters of the given string that have the smallest ASCII values
    smallest_chars = sorted_chars[:76]
    # sort the list in ascending order and return it
    return sorted(smallest_chars, key=ord)
