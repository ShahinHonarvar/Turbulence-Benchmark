
def return_n_smallest_chars(string):
    # Sort the string in ascending order
    sorted_string = sorted(string)
    # Create a list of exactly 21 characters
    smallest_chars = sorted_string[:21]
    # Return the list of smallest characters
    return smallest_chars
