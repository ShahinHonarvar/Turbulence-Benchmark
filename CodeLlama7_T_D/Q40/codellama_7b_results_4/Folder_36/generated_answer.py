
def return_n_smallest_chars(string):
    # Sort the string in ascending order based on ASCII values
    sorted_string = "".join(sorted(string))

    # Create a list of exactly 32 characters from the sorted string
    smallest_chars = sorted_string[:32]

    # Return the list of smallest characters in ascending order
    return smallest_chars
