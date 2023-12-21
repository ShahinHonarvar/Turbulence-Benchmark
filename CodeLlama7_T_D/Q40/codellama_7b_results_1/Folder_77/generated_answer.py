
def return_n_smallest_chars(my_string):
    # Sort the string in ascending order based on ASCII values
    sorted_string = sorted(my_string, key=ord)
    # Return the first 47 characters of the sorted string
    return sorted_string[:47]
