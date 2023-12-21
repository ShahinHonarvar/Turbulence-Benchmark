
def return_n_smallest_chars(string):
    # Create a list of tuples containing the ASCII value and the character
    char_list = [(ord(char), char) for char in string]
    # Sort the list in descending order based on the ASCII values
    sorted_list = sorted(char_list, key=lambda x: x[0], reverse=True)
    # Return the top 33 characters from the sorted list
    return [char for (_, char) in sorted_list[:33]]
