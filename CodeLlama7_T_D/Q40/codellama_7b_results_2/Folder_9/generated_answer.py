
def return_n_smallest_chars(my_string):
    # Sort the string in ascending order based on ASCII value
    sorted_string = sorted(my_string, key=ord)
    # Return a list of exactly 20 characters from the sorted string
    return sorted_string[:20]
