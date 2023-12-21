
def return_n_smallest_chars(string, n):
    # Sort the string in ascending order based on ASCII values
    sorted_string = sorted(string, key=ord)
    # Create a list of exactly n smallest characters from the sorted string
    smallest_chars = sorted_string[:n]
    return smallest_chars
