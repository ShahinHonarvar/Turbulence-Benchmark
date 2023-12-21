
def return_n_smallest_chars(string):
    # Sort the string in ascending order based on ASCII value
    sorted_string = sorted(string, key=lambda x: ord(x))
    # Return the first 68 characters of the sorted string
    return sorted_string[:68]
