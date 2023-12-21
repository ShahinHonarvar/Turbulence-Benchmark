
def return_n_smallest_chars(string, n=46):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(c, ord(c)) for c in string]
    # Sort the list in descending order based on the ASCII values
    sorted_list = sorted(char_list, key=lambda x: -x[1])
    # Return the top n characters from the sorted list
    return [tup[0] for tup in sorted_list[:n]]
