
def return_n_smallest_chars(my_string):
    # sort the string in ascending order based on ASCII values
    sorted_string = sorted(my_string, key=ord)
    # create a list of exactly 46 characters from the sorted string
    smallest_chars = sorted_string[:46]
    # return the list of smallest characters in descending order
    return smallest_chars[::-1]
