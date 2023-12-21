
def return_n_smallest_chars(string, n=6):
    # Create a list of tuples containing the ASCII value and the character itself
    char_list = [(ord(char), char) for char in string]
    # Sort the list in descending order based on the ASCII value
    sorted_list = sorted(char_list, key=lambda x: x[0], reverse=True)
    # Return the top n characters from the sorted list
    return [char for (_, char) in sorted_list[:n]]
