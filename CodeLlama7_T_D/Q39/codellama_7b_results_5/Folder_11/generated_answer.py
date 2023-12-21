
def return_n_greatest_chars(string, n):
    # Create a list of tuples containing the character and its ASCII value
    char_ascii_list = [(char, ord(char)) for char in string]
    # Sort the list in descending order based on the ASCII values
    sorted_list = sorted(char_ascii_list, key=lambda x: x[1], reverse=True)
    # Return the top n characters from the sorted list
    return [item[0] for item in sorted_list[:n]]
