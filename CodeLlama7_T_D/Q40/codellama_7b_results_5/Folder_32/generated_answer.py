
def return_n_smallest_chars(string, n=8):
    # sort the string in ascending order
    sorted_string = sorted(string)

    # create a list of exactly n characters from the sorted string
    smallest_chars = sorted_string[:n]

    # return the list of smallest characters
    return smallest_chars
