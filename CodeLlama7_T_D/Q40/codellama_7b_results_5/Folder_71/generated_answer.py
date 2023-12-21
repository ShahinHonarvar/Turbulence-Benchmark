
def return_n_smallest_chars(string):
    # sort the characters in the string based on their ASCII values
    sorted_chars = sorted(string, key=ord)
    # create a list of exactly 14 characters from the sorted list
    n_smallest_chars = sorted_chars[:14]
    # return the list of 14 smallest characters in ascending order
    return n_smallest_chars
