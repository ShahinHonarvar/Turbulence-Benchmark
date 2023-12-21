import sys
def return_n_smallest_chars(s):
    # sort the list
    char_list = sorted(set(s))
    # create a list of 84 characters
    return char_list[:84]
