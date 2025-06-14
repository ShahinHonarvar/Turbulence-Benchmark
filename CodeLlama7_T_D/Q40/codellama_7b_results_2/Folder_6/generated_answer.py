
def return_n_smallest_chars(string, n):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(char, ord(char)) for char in string]
    # Sort the list in descending order based on the ASCII values
    sorted_list = sorted(char_list, key=lambda x: x[1], reverse=True)
    # Return the top n characters from the sorted list
    return [char for (char, ord) in sorted_list[:n]]
