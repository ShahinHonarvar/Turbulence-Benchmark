
def return_n_smallest_chars(my_string):
    # sort the string in ascending order based on ASCII values
    sorted_string = sorted(my_string, key=ord)
    # create a list of exactly 48 characters from the sorted string
    smallest_chars = sorted_string[:48]
    return smallest_chars
