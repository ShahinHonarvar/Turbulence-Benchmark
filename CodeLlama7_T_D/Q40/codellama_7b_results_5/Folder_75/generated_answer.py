
def return_n_smallest_chars(my_string, n):
    # sort the string in ascending order based on ASCII values
    sorted_string = sorted(my_string)
    # create a list of exactly 2 characters of the given string that have the smallest ASCII values
    smallest_2_chars = sorted_string[:2]
    return smallest_2_chars
