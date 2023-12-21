
def return_n_smallest_chars(string):
    # Create a dictionary with the ASCII values of each character in the string as keys and the characters themselves as values
    ascii_values = {ord(char): char for char in string}

    # Sort the dictionary by key (ASCII value) in descending order
    sorted_dict = sorted(ascii_values.items(), reverse=True)

    # Create a list of exactly 39 characters from the sorted dictionary
    n_smallest_chars = [char for ascii, char in sorted_dict[:39]]

    # Return the list of 39 smallest ASCII characters
    return n_smallest_chars
