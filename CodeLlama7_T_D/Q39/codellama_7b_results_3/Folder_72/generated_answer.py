
def return_n_greatest_chars(s, n):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(c, ord(c)) for c in s]
    # Sort the list in descending order based on the ASCII values
    char_list.sort(key=lambda x: -x[1])
    # Return the top n characters from the sorted list
    return [char_tuple[0] for char_tuple in char_list[:n]]
