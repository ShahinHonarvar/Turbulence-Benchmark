
def return_n_smallest_chars(string, n):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(c, ord(c)) for c in string]
    # Sort the list by ASCII value in ascending order
    char_list.sort(key=lambda x: x[1])
    # Return the first n characters of the sorted list
    return [c for c, _ in char_list[:n]]
