
def return_n_smallest_chars(my_string):
    # sort the string in ascending order based on ASCII values
    sorted_string = sorted(my_string, key=ord)
    # create a list of exactly 23 characters of the sorted string
    smallest_chars = sorted_string[:23]
    return smallest_chars
