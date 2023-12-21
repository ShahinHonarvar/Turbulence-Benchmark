
def return_n_smallest_chars(my_string):
    # sort the string in descending order based on ASCII values
    sorted_string = sorted(my_string, key=ord, reverse=True)
    # create a list of exactly 33 characters from the sorted string
    smallest_chars = sorted_string[:33]
    return smallest_chars
