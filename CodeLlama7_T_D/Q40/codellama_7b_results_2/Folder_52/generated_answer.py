
def return_n_smallest_chars(my_string):
    # Sort the string in ascending order based on ASCII values
    sorted_string = sorted(my_string)
    # Create a list of exactly 68 characters from the sorted string
    n_smallest_chars = sorted_string[:68]
    return n_smallest_chars
