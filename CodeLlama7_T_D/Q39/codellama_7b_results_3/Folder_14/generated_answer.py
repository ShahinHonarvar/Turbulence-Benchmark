
def return_n_greatest_chars(my_string, n):
    """
    Returns the sorted list of exactly n characters of the given string that have the greatest ASCII values.
    Parameters:
    my_string (str): A string of distinct characters.
    n (int): The number of characters to return.

    Returns:

    sorted_list (list): A list of the n characters with the greatest ASCII values, sorted in ascending order.

    """

    # Create a list of all the characters in the string
    char_list = list(my_string)

    # Sort the list of characters by their ASCII values in descending order
    char_list.sort(key=ord, reverse=True)

    # Return the top n characters from the sorted list
    return char_list[:n]
