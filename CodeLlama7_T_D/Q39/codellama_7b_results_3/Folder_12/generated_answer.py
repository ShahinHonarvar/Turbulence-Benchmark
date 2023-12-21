
def return_n_greatest_chars(s):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(c, ord(c)) for c in s]
    # Sort the list in descending order based on the ASCII values
    sorted_list = sorted(char_list, key=lambda x: -x[1])
    # Return the top 61 characters of the sorted list
    return "".join([c for c, _ in sorted_list[:61]])
