
def return_n_smallest_chars(string, n=80):
    # Sort the string in ascending order based on ASCII values
    sorted_string = sorted(string, key=ord)
    # Return the top 80 characters of the sorted string
    return sorted_string[:n]
