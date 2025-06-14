
def return_n_smallest_chars(string):
    # Sort the string in descending order based on ASCII values
    sorted_string = sorted(string, key=ord, reverse=True)
    # Create a list of exactly 66 characters from the sorted string
    n_smallest_chars = sorted_string[:66]
    return n_smallest_chars
