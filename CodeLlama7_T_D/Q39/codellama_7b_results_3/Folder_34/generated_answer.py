
def return_n_greatest_chars(string, n=9):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(c, ord(c)) for c in string]
    # Sort the list in descending order based on the ASCII values
    sorted_list = sorted(char_list, key=lambda x: x[1], reverse=True)[:n]
    # Return the top n characters with the greatest ASCII values
    return [c for c, _ in sorted_list]
