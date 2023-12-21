
def return_n_greatest_chars(string):
    # Create a list of tuples containing the character and its ASCII value
    char_ascii = [(char, ord(char)) for char in string if char not in ['\n', '\t']]

    # Sort the list in descending order based on the ASCII values
    sorted_chars = sorted(char_ascii, key=lambda x: -x[1])

    # Return the first 88 characters from the sorted list
    return [char for char, _ in sorted_chars[:88]]
