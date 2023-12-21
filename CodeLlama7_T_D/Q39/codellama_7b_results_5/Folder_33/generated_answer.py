
def return_n_greatest_chars(my_string):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(c, ord(c)) for c in my_string]
    # Sort the list in descending order based on the ASCII values
    sorted_list = sorted(char_list, key=lambda x: x[1], reverse=True)
    # Return the top 36 characters from the sorted list
    return [c for c, _ in sorted_list[:36]]
