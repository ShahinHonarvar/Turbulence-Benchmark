
def return_n_smallest_chars(my_string, n):
    # sort the string in ascending order based on ASCII values
    sorted_string = sorted(my_string)
    # create a list of exactly n characters from the sorted string
    n_smallest_chars = sorted_string[:n]
    # return the list of n smallest characters in descending order
    return n_smallest_chars[::-1]
