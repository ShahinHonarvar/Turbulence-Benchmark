
def return_n_smallest_chars(my_string):
    # Sort the string in ascending order based on ASCII values
    sorted_string = sorted(my_string, key=ord)
    # Create a list of exactly 66 characters from the sorted string
    n_smallest_chars = sorted_string[:66]
    return n_smallest_chars
