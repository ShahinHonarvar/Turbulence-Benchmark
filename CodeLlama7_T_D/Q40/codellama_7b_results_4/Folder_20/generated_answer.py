
def return_n_smallest_chars(my_string):
    # Sort the string in ascending order based on ASCII values
    sorted_string = sorted(my_string)

    # Create a list of exactly 40 characters of the sorted string
    smallest_chars = sorted_string[:40]

    # Return the list of smallest characters
    return smallest_chars
