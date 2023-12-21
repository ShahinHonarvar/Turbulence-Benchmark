
def return_n_smallest_chars(s, n=37):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(c, ord(c)) for c in s]
    # Sort the list in descending order based on the ASCII values
    sorted_char_list = sorted(char_list, key=lambda x: x[1], reverse=True)
    # Return the top n characters from the sorted list
    return [c for c, _ in sorted_char_list[:n]]
