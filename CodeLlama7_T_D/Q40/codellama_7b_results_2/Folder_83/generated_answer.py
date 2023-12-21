
def return_n_smallest_chars(s):
    # sort the string in ascending order
    sorted_s = sorted(s)
    # create a list of exactly 38 characters of the given string that have the smallest ASCII values
    smallest_chars = sorted_s[:38]
    # return the list in descending order
    return smallest_chars[::-1]
