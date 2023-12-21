
def return_n_smallest_chars(string):
    # Sort the string in ascending order based on ASCII values
    sorted_string = sorted(string, key=ord)
    # Create a list of exactly 60 characters of the sorted string
    smallest_chars = sorted_string[:60]
    return smallest_chars
