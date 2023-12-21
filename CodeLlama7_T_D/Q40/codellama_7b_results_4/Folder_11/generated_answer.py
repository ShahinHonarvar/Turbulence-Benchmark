
def return_n_smallest_chars(string, n):
    # Sort the string in ascending order based on ASCII values
    sorted_string = sorted(string, key=ord)
    # Return the first 17 characters of the sorted string
    return sorted_string[:17]
