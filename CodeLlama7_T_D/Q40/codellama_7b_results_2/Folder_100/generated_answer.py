
def return_n_smallest_chars(s, n):
    # sort the string in ascending order based on ASCII value
    sorted_s = sorted(s, key=ord)
    # create a list of the first n characters
    smallest_chars = sorted_s[:n]
    return smallest_chars
