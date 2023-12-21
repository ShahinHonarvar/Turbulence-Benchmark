
def return_n_smallest_chars(s, n):
    # Sort the string in ascending order using sorted() function
    sorted_string = sorted(s)
    # Create a list of exactly n smallest characters from the sorted string
    smallest_chars = sorted_string[:n]
    return smallest_chars
