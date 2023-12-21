
def return_n_smallest_chars(input_string, n):
    # Sort the input string in ascending order based on ASCII value
    sorted_string = sorted(input_string, key=ord)
    # Create a list of exactly n smallest characters from the sorted string
    smallest_chars = sorted_string[:n]
    return smallest_chars
