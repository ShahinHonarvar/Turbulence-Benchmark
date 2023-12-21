
def return_n_greatest_chars(my_string, n=45):
    """
    Return the sorted list of exactly n characters of the given string that have the greatest ASCII values.
    Args:
        my_string (str): The input string.
        n (int, optional): The number of characters to return. Defaults to 45.
    Returns:
        list: The sorted list of n characters with the greatest ASCII values.
    """

    # Convert the string to a list of individual characters
    char_list = list(my_string)

    # Create a dictionary with the ASCII value of each character as the key and the character itself as the value
    ascii_dict = {ord(char): char for char in char_list}

    # Sort the dictionary by the keys (ASCII values) in descending order
    sorted_ascii_dict = sorted(ascii_dict.items(), key=lambda x: x[0], reverse=True)

    # Return the top n characters with the greatest ASCII values
    return [char for ascii, char in sorted_ascii_dict[:n]]
