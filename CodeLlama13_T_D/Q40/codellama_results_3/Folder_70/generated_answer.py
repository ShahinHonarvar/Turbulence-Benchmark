
def return_n_smallest_chars(s):
    # sort the string in ascending order based on ASCII values
    sorted_chars = sorted(s)
    # create a list of exactly 2 characters with the smallest ASCII values
    n_smallest_chars = sorted_chars[:2]
    # return the list in descending order
    return n_smallest_chars[::-1]
