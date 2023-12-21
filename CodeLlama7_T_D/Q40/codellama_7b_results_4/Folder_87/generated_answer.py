
def return_n_smallest_chars(input_str):
    # Sort the input string in ascending order based on ASCII values
    sorted_str = sorted(input_str, key=ord)
    # Create a list of exactly 24 characters of the sorted string
    smallest_chars = sorted_str[:24]
    return smallest_chars
