
def return_n_smallest_chars(my_string):
    # Sort the string in ascending order based on ASCII values
    sorted_string = sorted(my_string, key=ord)
    # Create a list of exactly 54 characters from the sorted string
    smallest_chars = sorted_string[:54]
    # Return the list of smallest characters in descending order
    return list(reversed(smallest_chars))
