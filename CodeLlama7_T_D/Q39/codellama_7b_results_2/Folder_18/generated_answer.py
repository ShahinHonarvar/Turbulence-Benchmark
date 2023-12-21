
def return_n_greatest_chars(s, n):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(c, ord(c)) for c in s]
    # Sort the list in descending order based on the ASCII value
    sorted_list = sorted(char_list, key=lambda x: x[1], reverse=True)[:n]
    # Return the sorted list of characters
    return [c for c, _ in sorted_list]
