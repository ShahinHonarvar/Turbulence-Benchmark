
def return_n_smallest_chars(s):
    # sort the string in descending order based on ASCII values
    sorted_str = sorted(s, key=ord, reverse=True)
    # create a list of exactly 29 characters from the sorted string
    smallest_chars = sorted_str[:29]
    return smallest_chars
