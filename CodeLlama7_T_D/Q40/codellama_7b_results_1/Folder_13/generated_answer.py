
def return_n_smallest_chars(my_string):
    # Sort the string in ascending order
    sorted_string = sorted(my_string)
    # Create a list of exactly 31 characters of the given string that have the smallest ASCII values
    smallest_chars = sorted_string[:31]
    return smallest_chars
