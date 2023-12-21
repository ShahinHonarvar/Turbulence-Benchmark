
def return_n_greatest_chars(string):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(c, ord(c)) for c in string]
    # Sort the list by ASCII value in descending order
    sorted_char_list = sorted(char_list, key=lambda x: x[1], reverse=True)
    # Return the first 34 characters of the sorted list
    return "".join([c for c, _ in sorted_char_list[:34]])
