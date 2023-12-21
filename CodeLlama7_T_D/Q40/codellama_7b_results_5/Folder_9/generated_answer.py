
def return_n_smallest_chars(string, n):
    # Create a list of tuples containing the ASCII value and character
    char_list = [(ord(char), char) for char in string]
    # Sort the list in ascending order based on the ASCII values
    sorted_list = sorted(char_list)
    # Return the top 20 characters from the sorted list
    return [char for (_, char) in sorted_list[:n]]
