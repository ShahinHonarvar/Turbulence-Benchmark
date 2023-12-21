
def return_n_smallest_chars(string, n=19):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(c, ord(c)) for c in string]
    # Sort the list by ASCII value in ascending order
    sorted_list = sorted(char_list, key=lambda x: x[1])
    # Return the top n characters from the sorted list
    return [x[0] for x in sorted_list[:n]]
