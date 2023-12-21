
def return_n_smallest_chars(my_string):
    # sort the string in descending order based on ASCII values
    sorted_list = sorted(my_string, key=ord, reverse=True)
    # create a list of exactly 77 characters of the sorted string
    smallest_chars = sorted_list[:77]
    return smallest_chars
