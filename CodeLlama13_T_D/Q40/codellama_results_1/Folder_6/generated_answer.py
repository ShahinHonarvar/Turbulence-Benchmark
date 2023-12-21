
def return_n_smallest_chars(string):
    # Create a list of tuples, where each tuple contains the ASCII value and the character
    char_ascii = [(ord(char), char) for char in string]

    # Sort the list in descending order based on the ASCII values
    sorted_list = sorted(char_ascii, key=lambda x: -x[0])

    # Create a new list with exactly 47 characters of the given string that have the smallest ASCII values
    n_smallest_chars = [char for (_, char) in sorted_list[:47]]

    return n_smallest_chars
