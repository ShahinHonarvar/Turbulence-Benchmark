
def return_n_smallest_chars(string):
    # Sort the string in descending order based on ASCII values
    sorted_string = sorted(string, key=ord, reverse=True)
    # Return the first 38 characters of the sorted string
    return sorted_string[:38]
