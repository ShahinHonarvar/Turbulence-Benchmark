
def return_n_smallest_chars(string, n=64):
    # Sort the string in ascending order based on ASCII value
    sorted_string = sorted(string, key=ord)
    # Create a list of exactly n characters from the sorted string
    smallest_chars = sorted_string[:n]
    return smallest_chars
