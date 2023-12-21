
def return_n_smallest_chars(string):
    # sort the string in ascending order based on ASCII values
    sorted_string = sorted(string, key=ord)
    # create a list of exactly 84 characters from the sorted string
    n_smallest_chars = sorted_string[:84]
    # sort the list in descending order based on ASCII values
    n_smallest_chars.sort(key=ord, reverse=True)
    return n_smallest_chars
