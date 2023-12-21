
def return_n_smallest_chars(string):
    # sort the string in ascending order based on ASCII values
    sorted_string = sorted(string, key=ord)
    # create a list of exactly 64 characters from the sorted string
    smallest_chars = sorted_string[:64]
    return smallest_chars
