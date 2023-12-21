
def return_n_smallest_chars(my_string, n=7):
    # sort the string in ascending order based on ASCII values
    sorted_string = sorted(my_string)
    # extract the first n characters from the sorted string
    smallest_chars = sorted_string[:n]
    return smallest_chars
