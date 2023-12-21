
def return_n_smallest_chars(string, n):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(c, ord(c)) for c in string]
    # Sort the list in descending order based on the ASCII value
    sorted_list = sorted(char_list, key=lambda x: x[1], reverse=True)
    # Return the top n characters in the sorted list
    return [c for c, _ in sorted_list[:n]]
