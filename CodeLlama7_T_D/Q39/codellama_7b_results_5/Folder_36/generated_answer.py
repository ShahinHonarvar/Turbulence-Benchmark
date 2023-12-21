
def return_n_greatest_chars(my_string, n):
    # Check if 'n' is a positive integer
    if not (isinstance(n, int) and n > 0):
        raise ValueError("'n' must be a positive integer")
    # Create a list of characters from the input string
    char_list = [char for char in my_string]
    # Sort the list of characters by their ASCII values in descending order
    sorted_list = sorted(char_list, key=ord, reverse=True)
    # Return the top 'n' elements of the sorted list
    return sorted_list[:n]
