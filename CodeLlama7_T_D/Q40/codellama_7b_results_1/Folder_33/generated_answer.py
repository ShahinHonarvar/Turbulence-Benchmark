
def return_n_smallest_chars(string):
    # Create a list of tuples containing (ASCII value, character)
    char_list = [(ord(c), c) for c in string]
    # Sort the list in descending order based on ASCII value
    char_list.sort(key=lambda x: x[0], reverse=True)
    # Return the top 36 characters from the sorted list
    return [char for (_, char) in char_list[:36]]
