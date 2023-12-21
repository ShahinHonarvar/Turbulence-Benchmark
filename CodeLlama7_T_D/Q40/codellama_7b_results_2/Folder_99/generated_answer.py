
def return_n_smallest_chars(s):
    # Create a list of tuples containing the ASCII values and the corresponding characters
    ascii_values = [(ord(c), c) for c in s]
    # Sort the list in descending order based on the ASCII values
    sorted_ascii_values = sorted(ascii_values, key=lambda x: x[0], reverse=True)
    # Return a list of exactly 35 characters of the given string that have the smallest ASCII values
    return [c for c, _ in sorted_ascii_values[:35]]
