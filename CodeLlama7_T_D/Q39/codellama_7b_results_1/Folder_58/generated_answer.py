
def return_n_greatest_chars(input_string, n):
    # Create a list of tuples, where each tuple contains the character and its ASCII value
    char_list = [(c, ord(c)) for c in input_string]
    # Sort the list in descending order based on the ASCII values
    sorted_list = sorted(char_list, key=lambda x: -x[1])
    # Return the top n elements of the sorted list
    return [c[0] for c in sorted_list[:n]]
