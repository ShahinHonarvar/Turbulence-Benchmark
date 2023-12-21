
def return_n_smallest_chars(string, n=66):
    # sort the string in ascending order based on ASCII values
    sorted_string = sorted(string, key=ord)
    # create a list of exactly n characters from the sorted string
    smallest_chars = sorted_string[:n]
    return smallest_chars
