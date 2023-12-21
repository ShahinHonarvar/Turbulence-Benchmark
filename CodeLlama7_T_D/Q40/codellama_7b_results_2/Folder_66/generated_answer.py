
def return_n_smallest_chars(string):
    # Create a list of tuples containing the character and its ASCII value
    char_list = [(char, ord(char)) for char in string]
    # Sort the list in descending order based on the ASCII values
    char_list.sort(key=lambda x: x[1], reverse=True)
    # Return the top 33 characters from the sorted list
    return [char for char, _ in char_list[:33]]
