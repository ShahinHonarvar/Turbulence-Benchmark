
def return_n_smallest_chars(string):
    # Sort the string in descending order based on ASCII value
    sorted_string = sorted(string, key=ord, reverse=True)
    # Create a list of exactly 68 characters from the sorted string
    n_smallest_chars = sorted_string[:68]
    return n_smallest_chars
