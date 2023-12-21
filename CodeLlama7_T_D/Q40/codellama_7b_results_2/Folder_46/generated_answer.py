
def return_n_smallest_chars(string, n=54):
    # Sort the string in descending order based on ASCII value
    sorted_string = sorted(string, key=ord, reverse=True)
    # Create a list of exactly n characters from the sorted string
    smallest_chars = sorted_string[:n]
    return smallest_chars
