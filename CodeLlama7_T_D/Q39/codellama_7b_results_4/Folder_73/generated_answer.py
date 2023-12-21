
def return_n_greatest_chars(input_string, n=80):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(c, ord(c)) for c in input_string]
    # Sort the list in descending order based on the ASCII values
    sorted_list = sorted(char_list, key=lambda x: x[1], reverse=True)[:n]
    return [x[0] for x in sorted_list]
