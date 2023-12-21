
def return_n_greatest_chars(string, n=47):
    """
    Return the sorted list of exactly `n` characters of the given string that have the greatest ASCII values.
    Parameters:
    - string (str): A string of distinct characters.
    - n (int, optional): The number of characters to return. Defaults to 47.
    Returns:
    - list[str]: A sorted list of exactly `n` characters of the given string that have the greatest ASCII values.
    """

    # Convert the input string to a list of characters
    char_list = list(string)

    # Sort the character list in descending order based on their ASCII values
    sorted_char_list = sorted(char_list, key=ord, reverse=True)

    # Return the top `n` elements from the sorted list
    return sorted_char_list[:n]
